/**
 * Inline Editor for The Freedom Paradox
 *
 * Include this script in any HTML page to enable:
 * - Toggle edit mode (pencil button)
 * - Click any text to edit inline
 * - Save commits the page to GitHub via the Contents API
 * - GitHub PAT stored in localStorage (entered once)
 *
 * Usage: <script src="editor.js" data-repo="PlayfulProcess/freedom-paradox" data-branch="claude/business-metrics-dashboard-Y2FlB"></script>
 */

(function () {
  const SCRIPT = document.currentScript;
  const REPO = SCRIPT?.getAttribute('data-repo') || 'PlayfulProcess/freedom-paradox';
  const BRANCH = SCRIPT?.getAttribute('data-branch') || 'master';
  const TOKEN_KEY = 'fp_github_token';

  // Determine file path relative to repo root
  // We need the user to set data-path, or we infer from location
  const FILE_PATH = SCRIPT?.getAttribute('data-path') || inferPath();

  function inferPath() {
    // Try to guess the file path from the URL
    const url = window.location.pathname;
    // If served from GitHub Pages: /freedom-paradox/dashboard/index.html
    // If served locally: /path/to/freedom-paradox/dashboard/index.html
    const match = url.match(/(?:freedom-paradox\/)(.*)/);
    if (match) return match[1];
    // Fallback: just the filename
    const parts = url.split('/');
    const file = parts[parts.length - 1] || 'index.html';
    // Assume dashboard/ prefix
    return 'dashboard/' + file;
  }

  // ===== UI ELEMENTS =====

  // Floating toolbar
  const toolbar = document.createElement('div');
  toolbar.id = 'fp-editor-toolbar';
  toolbar.innerHTML = `
    <style>
      #fp-editor-toolbar {
        position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9999;
        display: flex; gap: 0.5rem; align-items: center;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      }
      .fp-btn {
        border: none; border-radius: 8px; cursor: pointer;
        font-size: 0.82rem; font-weight: 600; padding: 0.6rem 1rem;
        display: flex; align-items: center; gap: 0.4rem;
        transition: all 0.2s; box-shadow: 0 2px 8px rgba(0,0,0,0.3);
      }
      .fp-btn-edit {
        background: #238636; color: #fff;
      }
      .fp-btn-edit:hover { background: #2ea043; }
      .fp-btn-edit.active { background: #f85149; }
      .fp-btn-edit.active:hover { background: #da3633; }
      .fp-btn-save {
        background: #1f6feb; color: #fff; display: none;
      }
      .fp-btn-save:hover { background: #388bfd; }
      .fp-btn-save:disabled { opacity: 0.5; cursor: not-allowed; }
      .fp-btn-settings {
        background: #30363d; color: #8b949e; padding: 0.6rem;
      }
      .fp-btn-settings:hover { color: #e6edf3; }
      .fp-status {
        font-size: 0.75rem; color: #8b949e; padding: 0.3rem 0.6rem;
        background: #161b22; border: 1px solid #30363d; border-radius: 6px;
        display: none; max-width: 250px;
      }
      .fp-status.show { display: block; }
      .fp-status.error { color: #f85149; border-color: #f85149; }
      .fp-status.success { color: #3fb950; border-color: #3fb950; }

      /* Edit mode styles */
      body.fp-editing [contenteditable="true"] {
        outline: 2px dashed rgba(88,166,255,0.3);
        outline-offset: 2px;
        border-radius: 2px;
        min-height: 1em;
      }
      body.fp-editing [contenteditable="true"]:focus {
        outline: 2px solid #58a6ff;
        background: rgba(88,166,255,0.05);
      }
      body.fp-editing [contenteditable="true"]:hover {
        outline: 2px dashed rgba(88,166,255,0.6);
      }

      /* Token modal */
      #fp-token-modal {
        display: none; position: fixed; inset: 0; z-index: 10000;
        background: rgba(0,0,0,0.7); align-items: center; justify-content: center;
      }
      #fp-token-modal.show { display: flex; }
      #fp-token-modal .modal-box {
        background: #161b22; border: 1px solid #30363d; border-radius: 12px;
        padding: 2rem; max-width: 450px; width: 90%;
      }
      #fp-token-modal h3 { font-size: 1.1rem; color: #e6edf3; margin-bottom: 0.5rem; }
      #fp-token-modal p { font-size: 0.82rem; color: #8b949e; margin-bottom: 1rem; }
      #fp-token-modal input {
        width: 100%; padding: 0.6rem; background: #0d1117; border: 1px solid #30363d;
        border-radius: 6px; color: #e6edf3; font-size: 0.85rem; font-family: monospace;
      }
      #fp-token-modal input:focus { outline: none; border-color: #58a6ff; }
      #fp-token-modal .modal-actions {
        display: flex; gap: 0.5rem; margin-top: 1rem; justify-content: flex-end;
      }
      #fp-token-modal .modal-actions button {
        padding: 0.5rem 1rem; border-radius: 6px; border: none; cursor: pointer;
        font-size: 0.82rem; font-weight: 600;
      }
      #fp-token-modal .btn-cancel { background: #30363d; color: #8b949e; }
      #fp-token-modal .btn-save-token { background: #238636; color: #fff; }
      #fp-token-modal .btn-clear { background: #da3633; color: #fff; font-size: 0.75rem; padding: 0.3rem 0.6rem; }
    </style>

    <div class="fp-status" id="fp-status"></div>
    <button class="fp-btn fp-btn-save" id="fp-save" title="Commit changes to GitHub">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Zm.176 4.823L9.75 4.81l-6.286 6.287a.253.253 0 0 0-.064.108l-.558 1.953 1.953-.558a.253.253 0 0 0 .108-.064Zm1.238-3.763a.25.25 0 0 0-.354 0L10.811 3.75l1.439 1.44 1.263-1.263a.25.25 0 0 0 0-.354Z"></path></svg>
      Save &amp; Commit
    </button>
    <button class="fp-btn fp-btn-edit" id="fp-toggle" title="Toggle edit mode">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M11.013 1.427a1.75 1.75 0 0 1 2.474 0l1.086 1.086a1.75 1.75 0 0 1 0 2.474l-8.61 8.61c-.21.21-.47.364-.756.445l-3.251.93a.75.75 0 0 1-.927-.928l.929-3.25c.081-.286.235-.547.445-.758l8.61-8.61Z"></path></svg>
      <span id="fp-toggle-label">Edit</span>
    </button>
    <button class="fp-btn fp-btn-settings" id="fp-settings" title="GitHub token settings">
      <svg width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0a8.2 8.2 0 0 0-2.6.42c-.36.12-.6.5-.48.86l.5 1.52a5.7 5.7 0 0 0-.96.56L3.14 2.5a.67.67 0 0 0-.88.18A8.1 8.1 0 0 0 .92 4.82c-.16.36 0 .78.34.94l1.44.72c-.1.34-.16.68-.2 1.02H1a.75.75 0 0 0-.75.75v.5A.75.75 0 0 0 1 9.5h1.5c.04.34.1.68.2 1.02l-1.44.72c-.34.16-.5.58-.34.94a8.1 8.1 0 0 0 1.34 2.14c.24.3.66.36.96.14l1.22-.86c.3.22.62.4.96.56l-.5 1.52c-.12.36.12.74.48.86A8.2 8.2 0 0 0 8 16a8.2 8.2 0 0 0 2.6-.42c.36-.12.6-.5.48-.86l-.5-1.52c.34-.16.66-.34.96-.56l1.22.86c.3.22.72.16.96-.14a8.1 8.1 0 0 0 1.34-2.14c.16-.36 0-.78-.34-.94l-1.44-.72c.1-.34.16-.68.2-1.02H15a.75.75 0 0 0 .75-.75v-.5A.75.75 0 0 0 15 7.5h-1.5c-.04-.34-.1-.68-.2-1.02l1.44-.72c.34-.16.5-.58.34-.94a8.1 8.1 0 0 0-1.34-2.14.67.67 0 0 0-.88-.18l-1.32.86a5.7 5.7 0 0 0-.96-.56l.5-1.52c.12-.36-.12-.74-.48-.86A8.2 8.2 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"></path></svg>
    </button>
  `;

  // Token modal
  const modal = document.createElement('div');
  modal.id = 'fp-token-modal';
  modal.innerHTML = `
    <div class="modal-box">
      <h3>GitHub Token</h3>
      <p>Enter a GitHub Personal Access Token with <code>repo</code> scope to enable saving. Token is stored in your browser's localStorage only.</p>
      <input type="password" id="fp-token-input" placeholder="ghp_xxxxxxxxxxxxxxxxxxxx" autocomplete="off">
      <p style="margin-top:0.8rem;font-size:0.75rem;">File: <code>${FILE_PATH}</code><br>Repo: <code>${REPO}</code> / Branch: <code>${BRANCH}</code></p>
      <div class="modal-actions">
        <button class="btn-clear" id="fp-clear-token">Clear token</button>
        <button class="btn-cancel" id="fp-cancel-modal">Cancel</button>
        <button class="btn-save-token" id="fp-save-token">Save</button>
      </div>
    </div>
  `;

  document.body.appendChild(toolbar);
  document.body.appendChild(modal);

  // ===== STATE =====
  let editMode = false;
  let dirty = false;
  const editableSelectors = 'p, h1, h2, h3, h4, li, td, .stat-value, .stat-label, .insight-box, .subtitle, .card-detail p, .card-detail .book-arg, .event-card p, .event-detail p, .rung-label, .rung-sublabel, .rung-card, .thesis-box p, .methodology-note p, header p';

  // ===== FUNCTIONS =====

  function getToken() {
    return localStorage.getItem(TOKEN_KEY);
  }

  function setStatus(msg, type) {
    const el = document.getElementById('fp-status');
    el.textContent = msg;
    el.className = 'fp-status show' + (type ? ' ' + type : '');
    if (type === 'success') setTimeout(() => el.classList.remove('show'), 3000);
  }

  function toggleEditMode() {
    editMode = !editMode;
    const btn = document.getElementById('fp-toggle');
    const label = document.getElementById('fp-toggle-label');
    const saveBtn = document.getElementById('fp-save');

    if (editMode) {
      document.body.classList.add('fp-editing');
      btn.classList.add('active');
      label.textContent = 'Stop Editing';
      saveBtn.style.display = 'flex';
      // Make elements editable
      document.querySelectorAll(editableSelectors).forEach(el => {
        // Skip toolbar/modal elements
        if (el.closest('#fp-editor-toolbar') || el.closest('#fp-token-modal')) return;
        el.setAttribute('contenteditable', 'true');
        el.addEventListener('input', markDirty);
      });
      setStatus('Click any text to edit', '');
    } else {
      document.body.classList.remove('fp-editing');
      btn.classList.remove('active');
      label.textContent = 'Edit';
      if (!dirty) saveBtn.style.display = 'none';
      document.querySelectorAll('[contenteditable]').forEach(el => {
        el.removeAttribute('contenteditable');
      });
      if (!dirty) {
        document.getElementById('fp-status').classList.remove('show');
      }
    }
  }

  function markDirty() {
    dirty = true;
    document.getElementById('fp-save').style.display = 'flex';
    setStatus('Unsaved changes', '');
  }

  async function saveToGitHub() {
    const token = getToken();
    if (!token) {
      document.getElementById('fp-token-modal').classList.add('show');
      return;
    }

    const saveBtn = document.getElementById('fp-save');
    saveBtn.disabled = true;
    setStatus('Saving...', '');

    try {
      // Remove contenteditable and toolbar before capturing HTML
      document.querySelectorAll('[contenteditable]').forEach(el => {
        el.removeAttribute('contenteditable');
      });
      const toolbarEl = document.getElementById('fp-editor-toolbar');
      const modalEl = document.getElementById('fp-token-modal');
      const scriptEl = document.querySelector('script[src="editor.js"]');
      toolbarEl.style.display = 'none';
      modalEl.style.display = 'none';

      // Capture clean HTML
      const html = '<!DOCTYPE html>\n' + document.documentElement.outerHTML;

      // Restore toolbar
      toolbarEl.style.display = '';
      modalEl.style.display = '';

      // Get current file SHA
      const getResp = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}?ref=${BRANCH}`, {
        headers: { 'Authorization': `token ${token}`, 'Accept': 'application/vnd.github.v3+json' }
      });

      if (!getResp.ok && getResp.status !== 404) {
        throw new Error(`GitHub API error: ${getResp.status} ${getResp.statusText}`);
      }

      const getData = getResp.ok ? await getResp.json() : null;
      const sha = getData?.sha;

      // Encode content
      // Use TextEncoder for proper UTF-8 handling
      const encoder = new TextEncoder();
      const bytes = encoder.encode(html);
      let binary = '';
      bytes.forEach(b => binary += String.fromCharCode(b));
      const content = btoa(binary);

      // Commit
      const putBody = {
        message: `Edit via browser: ${FILE_PATH.split('/').pop()}\n\nhttps://claude.ai/code/session_01CmzPvj6FH1ad9aaGzWbeXN`,
        content: content,
        branch: BRANCH,
      };
      if (sha) putBody.sha = sha;
      putBody.committer = {
        name: 'PlayfulProcess',
        email: '17236172+PlayfulProcess@users.noreply.github.com'
      };

      const putResp = await fetch(`https://api.github.com/repos/${REPO}/contents/${FILE_PATH}`, {
        method: 'PUT',
        headers: {
          'Authorization': `token ${token}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(putBody),
      });

      if (!putResp.ok) {
        const err = await putResp.json();
        throw new Error(err.message || `HTTP ${putResp.status}`);
      }

      const result = await putResp.json();
      dirty = false;
      setStatus('Committed: ' + result.commit.sha.substring(0, 7), 'success');

      // Re-enable editing if still in edit mode
      if (editMode) {
        document.querySelectorAll(editableSelectors).forEach(el => {
          if (el.closest('#fp-editor-toolbar') || el.closest('#fp-token-modal')) return;
          el.setAttribute('contenteditable', 'true');
        });
      }

    } catch (err) {
      setStatus('Error: ' + err.message, 'error');
      // Restore editability
      if (editMode) {
        document.querySelectorAll(editableSelectors).forEach(el => {
          if (el.closest('#fp-editor-toolbar') || el.closest('#fp-token-modal')) return;
          el.setAttribute('contenteditable', 'true');
        });
      }
    } finally {
      saveBtn.disabled = false;
    }
  }

  // ===== EVENT LISTENERS =====

  document.getElementById('fp-toggle').addEventListener('click', toggleEditMode);
  document.getElementById('fp-save').addEventListener('click', saveToGitHub);
  document.getElementById('fp-settings').addEventListener('click', () => {
    const input = document.getElementById('fp-token-input');
    input.value = getToken() || '';
    document.getElementById('fp-token-modal').classList.add('show');
  });
  document.getElementById('fp-cancel-modal').addEventListener('click', () => {
    document.getElementById('fp-token-modal').classList.remove('show');
  });
  document.getElementById('fp-save-token').addEventListener('click', () => {
    const token = document.getElementById('fp-token-input').value.trim();
    if (token) {
      localStorage.setItem(TOKEN_KEY, token);
      setStatus('Token saved', 'success');
    }
    document.getElementById('fp-token-modal').classList.remove('show');
  });
  document.getElementById('fp-clear-token').addEventListener('click', () => {
    localStorage.removeItem(TOKEN_KEY);
    document.getElementById('fp-token-input').value = '';
    setStatus('Token cleared', '');
  });

  // Close modal on outside click
  document.getElementById('fp-token-modal').addEventListener('click', (e) => {
    if (e.target.id === 'fp-token-modal') {
      document.getElementById('fp-token-modal').classList.remove('show');
    }
  });

  // Warn before leaving with unsaved changes
  window.addEventListener('beforeunload', (e) => {
    if (dirty) {
      e.preventDefault();
      e.returnValue = '';
    }
  });

})();
