/**
 * Annotator — highlight & note-taking for mdbook
 * Storage: IndexedDB (local) + JSON export/import (any cloud folder)
 */
(function () {
  'use strict';

  // ── Helpers ──────────────────────────────────────────────
  function uuid() {
    return crypto.randomUUID ? crypto.randomUUID() :
      'xxxx-xxxx-xxxx'.replace(/x/g, () => (Math.random() * 16 | 0).toString(16));
  }

  function getChapterKey() {
    // Use the page path as a stable key, e.g. "freedom-paradox/ch01-the-anthropic-clause.html"
    return location.pathname.replace(/^\//, '').replace(/\/$/, '') || 'index';
  }

  function getBookName() {
    var parts = getChapterKey().split('/');
    return parts.length > 1 ? parts[0] : 'home';
  }

  function toast(msg) {
    var el = document.createElement('div');
    el.className = 'annotator-toast';
    el.textContent = msg;
    document.body.appendChild(el);
    setTimeout(function () {
      el.style.opacity = '0';
      el.style.transition = 'opacity 0.3s';
      setTimeout(function () { el.remove(); }, 300);
    }, 2000);
  }

  // ── IndexedDB storage ───────────────────────────────────
  var DB_NAME = 'annotator';
  var DB_VERSION = 1;
  var STORE = 'highlights';
  var db = null;

  function openDB(cb) {
    if (db) return cb(db);
    var req = indexedDB.open(DB_NAME, DB_VERSION);
    req.onupgradeneeded = function (e) {
      var d = e.target.result;
      if (!d.objectStoreNames.contains(STORE)) {
        var store = d.createObjectStore(STORE, { keyPath: 'id' });
        store.createIndex('chapter', 'chapter', { unique: false });
      }
    };
    req.onsuccess = function (e) { db = e.target.result; cb(db); };
    req.onerror = function () { console.error('Annotator: IndexedDB error'); };
  }

  function getAllHighlights(cb) {
    openDB(function (d) {
      var tx = d.transaction(STORE, 'readonly');
      var all = tx.objectStore(STORE).getAll();
      all.onsuccess = function () { cb(all.result || []); };
    });
  }

  function getChapterHighlights(cb) {
    var key = getChapterKey();
    openDB(function (d) {
      var tx = d.transaction(STORE, 'readonly');
      var idx = tx.objectStore(STORE).index('chapter');
      var req = idx.getAll(key);
      req.onsuccess = function () { cb(req.result || []); };
    });
  }

  function saveHighlight(h, cb) {
    openDB(function (d) {
      var tx = d.transaction(STORE, 'readwrite');
      tx.objectStore(STORE).put(h);
      tx.oncomplete = function () { if (cb) cb(); };
    });
  }

  function deleteHighlight(id, cb) {
    openDB(function (d) {
      var tx = d.transaction(STORE, 'readwrite');
      tx.objectStore(STORE).delete(id);
      tx.oncomplete = function () { if (cb) cb(); };
    });
  }

  function importHighlights(items, cb) {
    openDB(function (d) {
      var tx = d.transaction(STORE, 'readwrite');
      var store = tx.objectStore(STORE);
      items.forEach(function (h) { store.put(h); });
      tx.oncomplete = function () { if (cb) cb(); };
    });
  }

  // ── Text anchoring ──────────────────────────────────────
  // We anchor highlights using surrounding text context (prefix + exact + suffix).
  // This survives minor edits better than DOM-based selectors.

  function getContext(range) {
    var text = range.toString();
    // Get prefix: up to 50 chars before the selection in the same parent
    var container = range.startContainer;
    var fullText = container.textContent || '';
    var startOffset = range.startOffset;
    var prefix = fullText.substring(Math.max(0, startOffset - 50), startOffset);

    // Get suffix: up to 50 chars after the selection
    var endContainer = range.endContainer;
    var endText = endContainer.textContent || '';
    var endOffset = range.endOffset;
    var suffix = endText.substring(endOffset, endOffset + 50);

    return { prefix: prefix, exact: text, suffix: suffix };
  }

  function findTextInContent(anchor) {
    var content = document.querySelector('.content main');
    if (!content) return null;

    var walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, null, false);
    var searchStr = anchor.exact;
    var node;
    var found = [];

    // Collect all text nodes and their positions
    while ((node = walker.nextNode())) {
      found.push(node);
    }

    // Try to find the exact text with context matching
    for (var i = 0; i < found.length; i++) {
      var n = found[i];
      var text = n.textContent;
      var idx = text.indexOf(searchStr);
      if (idx === -1) continue;

      // Check if context matches (fuzzy)
      var prefixMatch = !anchor.prefix || text.substring(Math.max(0, idx - 50), idx).indexOf(anchor.prefix.slice(-20)) !== -1;
      var suffixMatch = !anchor.suffix || text.substring(idx + searchStr.length, idx + searchStr.length + 50).indexOf(anchor.suffix.slice(0, 20)) !== -1;

      if (prefixMatch || suffixMatch || !anchor.prefix) {
        var range = document.createRange();
        range.setStart(n, idx);
        range.setEnd(n, idx + searchStr.length);
        return range;
      }
    }

    // Fallback: search across adjacent text nodes
    var fullContent = content.textContent || '';
    var searchIdx = fullContent.indexOf(searchStr);
    if (searchIdx === -1) return null;

    // If we found it in the full text, try to map back to DOM nodes
    walker = document.createTreeWalker(content, NodeFilter.SHOW_TEXT, null, false);
    var charCount = 0;
    var startNode = null, startOff = 0, endNode = null, endOff = 0;

    while ((node = walker.nextNode())) {
      var len = node.textContent.length;
      if (!startNode && charCount + len > searchIdx) {
        startNode = node;
        startOff = searchIdx - charCount;
      }
      if (startNode && charCount + len >= searchIdx + searchStr.length) {
        endNode = node;
        endOff = searchIdx + searchStr.length - charCount;
        break;
      }
      charCount += len;
    }

    if (startNode && endNode) {
      var r = document.createRange();
      r.setStart(startNode, startOff);
      r.setEnd(endNode, endOff);
      return r;
    }

    return null;
  }

  // ── Rendering highlights ────────────────────────────────
  function renderHighlight(range, highlightData) {
    var mark = document.createElement('mark');
    mark.className = 'annotator-highlight';
    mark.dataset.id = highlightData.id;
    if (highlightData.note) mark.classList.add('has-note');

    try {
      range.surroundContents(mark);
    } catch (e) {
      // Range spans multiple elements — wrap each text node
      var frag = range.extractContents();
      mark.appendChild(frag);
      range.insertNode(mark);
    }

    mark.addEventListener('click', function (e) {
      e.stopPropagation();
      showDetail(mark, highlightData);
    });

    return mark;
  }

  function renderAllHighlights() {
    // Clear existing marks first
    document.querySelectorAll('mark.annotator-highlight').forEach(function (m) {
      var parent = m.parentNode;
      while (m.firstChild) parent.insertBefore(m.firstChild, m);
      parent.removeChild(m);
      parent.normalize();
    });

    getChapterHighlights(function (highlights) {
      highlights.forEach(function (h) {
        var range = findTextInContent(h.anchor);
        if (range) {
          renderHighlight(range, h);
        }
      });
    });
  }

  // ── Selection popover ───────────────────────────────────
  var popover = null;

  function removePopover() {
    if (popover) { popover.remove(); popover = null; }
  }

  function removeDetail() {
    var d = document.querySelector('.annotator-detail');
    if (d) d.remove();
  }

  function showPopover(x, y, range) {
    removePopover();
    removeDetail();

    var div = document.createElement('div');
    div.className = 'annotator-popover';

    var btnHighlight = document.createElement('button');
    btnHighlight.textContent = 'Highlight';
    btnHighlight.addEventListener('click', function (e) {
      e.stopPropagation();
      createHighlight(range, '');
      removePopover();
    });

    var btnNote = document.createElement('button');
    btnNote.textContent = '+ Note';
    btnNote.addEventListener('click', function (e) {
      e.stopPropagation();
      removePopover();
      showNoteModal(range);
    });

    div.appendChild(btnHighlight);
    div.appendChild(btnNote);
    document.body.appendChild(div);

    // Position above selection
    var rect = div.getBoundingClientRect();
    div.style.left = Math.max(8, Math.min(x - rect.width / 2, window.innerWidth - rect.width - 8)) + 'px';
    div.style.top = Math.max(8, y - rect.height - 10) + 'px';
    popover = div;
  }

  // ── Note modal ──────────────────────────────────────────
  function showNoteModal(range, existingNote, onSave) {
    var text = range ? range.toString() : '';
    var overlay = document.createElement('div');
    overlay.className = 'annotator-note-modal';

    overlay.innerHTML =
      '<div class="annotator-note-modal-inner">' +
        '<h3>Add a note</h3>' +
        '<div class="annotator-quote-preview">"' + (text.length > 120 ? text.slice(0, 120) + '...' : text) + '"</div>' +
        '<textarea placeholder="Your note..."></textarea>' +
        '<div class="annotator-modal-actions">' +
          '<button class="annotator-btn-cancel">Cancel</button>' +
          '<button class="annotator-btn-save">Save</button>' +
        '</div>' +
      '</div>';

    var textarea = overlay.querySelector('textarea');
    if (existingNote) textarea.value = existingNote;

    overlay.querySelector('.annotator-btn-cancel').addEventListener('click', function () {
      overlay.remove();
    });

    overlay.querySelector('.annotator-btn-save').addEventListener('click', function () {
      var note = textarea.value.trim();
      if (onSave) {
        onSave(note);
      } else {
        createHighlight(range, note);
      }
      overlay.remove();
    });

    // Close on backdrop click
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) overlay.remove();
    });

    // Save on Ctrl/Cmd+Enter
    textarea.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
        overlay.querySelector('.annotator-btn-save').click();
      }
    });

    document.body.appendChild(overlay);
    textarea.focus();
  }

  // ── Create highlight ────────────────────────────────────
  function createHighlight(range, note) {
    var anchor = getContext(range);
    var h = {
      id: uuid(),
      chapter: getChapterKey(),
      book: getBookName(),
      anchor: anchor,
      note: note || '',
      createdAt: new Date().toISOString()
    };

    saveHighlight(h, function () {
      renderAllHighlights();
      toast('Highlight saved');
    });
  }

  // ── Detail tooltip (click on existing highlight) ───────
  function showDetail(mark, h) {
    removeDetail();
    removePopover();

    var div = document.createElement('div');
    div.className = 'annotator-detail';

    var html = '';
    if (h.note) {
      html += '<div class="annotator-detail-note">' + escapeHtml(h.note) + '</div>';
    }
    html += '<div class="annotator-detail-actions">';
    html += '<button class="annotator-btn-link">Copy Link</button>';
    html += '<button class="annotator-btn-edit">' + (h.note ? 'Edit Note' : 'Add Note') + '</button>';
    html += '<button class="annotator-btn-delete">Remove</button>';
    html += '</div>';
    div.innerHTML = html;

    // Copy shareable link (Text Fragment URL)
    div.querySelector('.annotator-btn-link').addEventListener('click', function () {
      var url = buildShareableURL(h);
      navigator.clipboard.writeText(url).then(function () {
        toast('Link copied');
      });
      div.remove();
    });

    // Edit / add note
    div.querySelector('.annotator-btn-edit').addEventListener('click', function () {
      div.remove();
      var fakeRange = { toString: function () { return h.anchor.exact; } };
      showNoteModal(fakeRange, h.note, function (newNote) {
        h.note = newNote;
        saveHighlight(h, function () {
          renderAllHighlights();
          toast('Note updated');
        });
      });
    });

    // Delete
    div.querySelector('.annotator-btn-delete').addEventListener('click', function () {
      deleteHighlight(h.id, function () {
        div.remove();
        renderAllHighlights();
        toast('Highlight removed');
      });
    });

    document.body.appendChild(div);
    var markRect = mark.getBoundingClientRect();
    var detailRect = div.getBoundingClientRect();
    div.style.left = Math.max(8, Math.min(
      markRect.left + markRect.width / 2 - detailRect.width / 2,
      window.innerWidth - detailRect.width - 8
    )) + 'px';
    div.style.top = (markRect.bottom + window.scrollY + 8) + 'px';
  }

  // ── Shareable URL builder ───────────────────────────────
  function buildShareableURL(h) {
    var base = location.origin + location.pathname;
    var text = encodeURIComponent(h.anchor.exact);

    // Use prefix/suffix for disambiguation when available
    var fragment = ':~:text=';
    if (h.anchor.prefix && h.anchor.prefix.length > 10) {
      fragment += encodeURIComponent(h.anchor.prefix.slice(-20)) + '-,';
    }
    fragment += text;
    if (h.anchor.suffix && h.anchor.suffix.length > 10) {
      fragment += ',-' + encodeURIComponent(h.anchor.suffix.slice(0, 20));
    }

    return base + '#' + fragment;
  }

  // ── Highlights panel (sidebar) ──────────────────────────
  var panel = null;

  function togglePanel() {
    if (panel) { panel.remove(); panel = null; return; }

    panel = document.createElement('div');
    panel.className = 'annotator-panel';

    var header = document.createElement('div');
    header.className = 'annotator-panel-header';
    header.innerHTML = '<h3>Highlights</h3><button aria-label="Close">&times;</button>';
    header.querySelector('button').addEventListener('click', function () {
      panel.remove(); panel = null;
    });

    var body = document.createElement('div');
    body.className = 'annotator-panel-body';

    var footer = document.createElement('div');
    footer.className = 'annotator-panel-footer';
    footer.innerHTML =
      '<button class="annotator-export-json">Export JSON</button>' +
      '<button class="annotator-export-md">Export Markdown</button>' +
      '<button class="annotator-export-csv">Export CSV</button>' +
      '<button class="annotator-import">Import</button>';

    panel.appendChild(header);
    panel.appendChild(body);
    panel.appendChild(footer);
    document.body.appendChild(panel);

    // Populate
    refreshPanel(body);

    // Wire up export/import
    footer.querySelector('.annotator-export-json').addEventListener('click', function () { exportJSON(); });
    footer.querySelector('.annotator-export-md').addEventListener('click', function () { exportMarkdown(); });
    footer.querySelector('.annotator-export-csv').addEventListener('click', function () { exportCSV(); });
    footer.querySelector('.annotator-import').addEventListener('click', function () { triggerImport(); });
  }

  function refreshPanel(body) {
    if (!body) body = panel && panel.querySelector('.annotator-panel-body');
    if (!body) return;

    getAllHighlights(function (highlights) {
      body.innerHTML = '';

      if (highlights.length === 0) {
        body.innerHTML = '<p style="color:#999; font-size:13px; text-align:center; padding:20px;">No highlights yet. Select text to get started.</p>';
        return;
      }

      // Group by book > chapter
      var grouped = {};
      highlights.sort(function (a, b) { return (b.createdAt || '').localeCompare(a.createdAt || ''); });

      highlights.forEach(function (h) {
        var key = h.book || 'unknown';
        if (!grouped[key]) grouped[key] = [];
        grouped[key].push(h);
      });

      Object.keys(grouped).forEach(function (book) {
        var bookTitle = document.createElement('div');
        bookTitle.style.cssText = 'font-size:11px; font-weight:600; text-transform:uppercase; letter-spacing:0.05em; color:#999; margin:12px 0 6px; padding-top:8px; border-top:1px solid #eee;';
        bookTitle.textContent = book.replace(/-/g, ' ');
        body.appendChild(bookTitle);

        grouped[book].forEach(function (h) {
          var item = document.createElement('div');
          item.className = 'annotator-panel-item';
          item.style.cursor = 'pointer';

          var quoteText = h.anchor.exact.length > 100 ? h.anchor.exact.slice(0, 100) + '...' : h.anchor.exact;
          var html = '<div class="annotator-panel-quote">"' + escapeHtml(quoteText) + '"</div>';
          if (h.note) {
            html += '<div class="annotator-panel-note">' + escapeHtml(h.note) + '</div>';
          }
          item.innerHTML = html;

          // Click to navigate to that chapter
          item.addEventListener('click', function () {
            var chapterUrl = location.origin + '/' + h.chapter;
            if (location.pathname.replace(/^\//, '') === h.chapter) {
              // Same page — scroll to highlight
              var mark = document.querySelector('mark[data-id="' + h.id + '"]');
              if (mark) mark.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } else {
              location.href = chapterUrl;
            }
          });

          body.appendChild(item);
        });
      });
    });
  }

  // ── Export functions ────────────────────────────────────
  function downloadFile(filename, content, mime) {
    var blob = new Blob([content], { type: mime });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }

  function exportJSON() {
    getAllHighlights(function (highlights) {
      var data = {
        exported: new Date().toISOString(),
        count: highlights.length,
        highlights: highlights
      };
      downloadFile('highlights.json', JSON.stringify(data, null, 2), 'application/json');
      toast('Exported ' + highlights.length + ' highlights');
    });
  }

  function exportMarkdown() {
    getAllHighlights(function (highlights) {
      var lines = ['# Highlights\n', 'Exported: ' + new Date().toISOString() + '\n'];
      var grouped = {};

      highlights.forEach(function (h) {
        var key = h.book || 'unknown';
        if (!grouped[key]) grouped[key] = [];
        grouped[key].push(h);
      });

      Object.keys(grouped).forEach(function (book) {
        lines.push('\n## ' + book.replace(/-/g, ' ') + '\n');
        grouped[book].forEach(function (h) {
          lines.push('> ' + h.anchor.exact + '\n');
          if (h.note) lines.push('**Note:** ' + h.note + '\n');
          lines.push('*Chapter: ' + h.chapter + ' | ' + (h.createdAt || '') + '*\n');
        });
      });

      downloadFile('highlights.md', lines.join('\n'), 'text/markdown');
      toast('Exported as Markdown');
    });
  }

  function exportCSV() {
    getAllHighlights(function (highlights) {
      var rows = [['Book', 'Chapter', 'Highlight', 'Note', 'Date'].join(',')];
      highlights.forEach(function (h) {
        rows.push([
          csvEscape(h.book || ''),
          csvEscape(h.chapter || ''),
          csvEscape(h.anchor.exact || ''),
          csvEscape(h.note || ''),
          csvEscape(h.createdAt || '')
        ].join(','));
      });
      downloadFile('highlights.csv', rows.join('\n'), 'text/csv');
      toast('Exported as CSV');
    });
  }

  function csvEscape(str) {
    if (str.indexOf(',') !== -1 || str.indexOf('"') !== -1 || str.indexOf('\n') !== -1) {
      return '"' + str.replace(/"/g, '""') + '"';
    }
    return str;
  }

  // ── Import ──────────────────────────────────────────────
  function triggerImport() {
    var input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    input.addEventListener('change', function () {
      var file = input.files[0];
      if (!file) return;
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var data = JSON.parse(reader.result);
          var items = data.highlights || data;
          if (!Array.isArray(items)) throw new Error('Invalid format');
          importHighlights(items, function () {
            renderAllHighlights();
            if (panel) refreshPanel();
            toast('Imported ' + items.length + ' highlights');
          });
        } catch (e) {
          toast('Import failed: invalid JSON');
        }
      };
      reader.readAsText(file);
    });
    input.click();
  }

  // ── Utility ─────────────────────────────────────────────
  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ── Toolbar button injection ────────────────────────────
  function addToolbarButton() {
    var menuBar = document.querySelector('.left-buttons') || document.querySelector('.menu-bar');
    if (!menuBar) return;

    var btn = document.createElement('button');
    btn.id = 'annotator-toggle';
    btn.setAttribute('aria-label', 'Highlights');
    btn.setAttribute('title', 'Highlights & Notes');
    btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>';
    btn.addEventListener('click', togglePanel);
    menuBar.appendChild(btn);
  }

  // ── Event listeners ─────────────────────────────────────
  function init() {
    addToolbarButton();
    renderAllHighlights();

    // Show popover on text selection
    document.addEventListener('mouseup', function (e) {
      // Ignore clicks on annotator UI elements
      if (e.target.closest('.annotator-popover, .annotator-detail, .annotator-note-modal, .annotator-panel')) return;

      removePopover();

      var sel = window.getSelection();
      if (!sel || sel.isCollapsed || !sel.toString().trim()) return;

      // Only allow selections within content area
      var range = sel.getRangeAt(0);
      var content = document.querySelector('.content main');
      if (!content || !content.contains(range.commonAncestorContainer)) return;

      var rect = range.getBoundingClientRect();
      showPopover(rect.left + rect.width / 2, rect.top + window.scrollY, range.cloneRange());
    });

    // Touch support for mobile
    document.addEventListener('touchend', function (e) {
      if (e.target.closest('.annotator-popover, .annotator-detail, .annotator-note-modal, .annotator-panel')) return;

      // Delay to let the browser finalize the selection
      setTimeout(function () {
        var sel = window.getSelection();
        if (!sel || sel.isCollapsed || !sel.toString().trim()) return;

        var range = sel.getRangeAt(0);
        var content = document.querySelector('.content main');
        if (!content || !content.contains(range.commonAncestorContainer)) return;

        var rect = range.getBoundingClientRect();
        showPopover(rect.left + rect.width / 2, rect.top + window.scrollY, range.cloneRange());
      }, 300);
    });

    // Dismiss popovers on click outside
    document.addEventListener('mousedown', function (e) {
      if (!e.target.closest('.annotator-popover')) removePopover();
      if (!e.target.closest('.annotator-detail, mark.annotator-highlight')) removeDetail();
    });

    // Keyboard shortcut: Escape closes panel/modals
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        removePopover();
        removeDetail();
        var modal = document.querySelector('.annotator-note-modal');
        if (modal) modal.remove();
        if (panel) { panel.remove(); panel = null; }
      }
    });
  }

  // ── Start ───────────────────────────────────────────────
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
