# Chapter 3: Free as in Freedom

Before there was a movement, there was a printer.

In the late 1970s, Richard Stallman was a programmer at MIT's Artificial Intelligence Laboratory — one of the most creative computing environments on Earth. The lab ran on a culture of radical openness. If a program broke, you fixed it. If someone wrote something useful, they shared it. Source code circulated the way academic papers circulate: freely, because knowledge shared is knowledge multiplied.

Then the lab got a new printer. A Xerox machine. It jammed constantly, and in the old culture, that wouldn't have been a problem — someone would simply look at the source code for the printer driver, find the bug, and fix it. Stallman had done exactly this with a previous printer, adding code that alerted users when their print jobs were done or when paper was jammed.

But the Xerox printer came with a catch. Its software was proprietary. The source code was locked. When Stallman asked a researcher at Carnegie Mellon for a copy — someone who had access — the researcher refused. He had signed a non-disclosure agreement.

[QUOTE NEEDED: Stallman's account of this moment — what he felt, what it crystallized]

This was not an isolated incident. It was a symptom of a tectonic shift. Throughout the 1950s, 1960s, and into the 1970s, sharing software had simply been how computing worked. The SHARE users group — its name says everything — was founded in 1955 and began distributing free software that same year, making it one of the oldest collaborative institutions in computing history. Universities passed code around like recipes. When Ken Thompson designed the first UNIX operating system at Bell Labs in the late 1960s, it was distributed freely to universities and research labs worldwide. Users could read it, modify it, learn from it.

Then the lawyers arrived.

A series of legal decisions in the late 1970s and early 1980s established that software could be copyrighted. Bell Labs copyrighted UNIX in 1979. Non-disclosure agreements proliferated. Proprietary licenses became standard. The best programmers were recruited out of universities into corporate shops where their work was locked behind legal walls.

What had been the default — sharing — became the exception. What had been the exception — restriction — became the default.

Stallman saw this reversal clearly, and he refused to accept it. In 1983, he announced the GNU Project: an audacious effort to build a complete, free operating system from scratch. Not free as in price — free as in freedom. The distinction would define everything that followed.

---

In early 1985, Stallman published "The GNU Manifesto" — a document that reads less like a technical specification and more like a political declaration. Its arguments are moral, not commercial. Software, Stallman insisted, is a form of knowledge. Restricting it harms everyone. Programmers can and should find ways to make a living that don't require locking up the tools other people need.

[QUOTE NEEDED: Key passage from the GNU Manifesto on why software should be free]

That same year, he founded the Free Software Foundation. And at the foundation's core he placed four principles — the Four Freedoms — that would become the ethical bedrock of the entire movement:

**Freedom 0:** The freedom to run the program for any purpose.

**Freedom 1:** The freedom to study how the program works and modify it.

**Freedom 2:** The freedom to redistribute copies.

**Freedom 3:** The freedom to distribute copies of your modified versions.

Read these carefully. They are not suggestions for good business practice. They are claims about what humans are *owed* in their relationship to the tools they use. Stallman wasn't arguing that free software made better products or bigger profits. He was arguing that restricting software is ethically wrong — a violation of the user's autonomy.

This moral framing would later be deliberately discarded by the "open source" rebranding of 1998. But the framing matters enormously for the question this book is ultimately asking. Because the Four Freedoms contain an assumption so deep it was invisible in 1985: the thing being freed is benign.

A text editor is benign. A compiler is benign. An operating system is benign. When Stallman wrote Freedom 0 — "to run the program for any purpose" — the "any purpose" was limited by the nature of what software could do. Nobody was going to use Emacs for mass surveillance. Nobody was going to deploy GCC as an autonomous weapon.

The question this book will return to, again and again, is what happens when the Four Freedoms meet a technology where "any purpose" includes purposes that could destabilize civilization.

But in 1985, that question was forty years away. First, Stallman had an operating system to build.

---

The GNU Project was an extraordinary act of construction. Stallman and a growing community of contributors built the tools of a complete operating system, piece by piece. GCC — the GNU Compiler Collection — became the standard compiler for the computing world. Emacs became one of the most powerful text editors ever created. GNU Coreutils, the shell, the libraries — component after component, they built it all.

But they needed one more thing. The most critical piece of any operating system: the kernel, the core program that manages hardware resources and allows everything else to run. The GNU Project's kernel — called GNU Hurd — proved fiendishly difficult to complete. For years, it was the missing foundation of an otherwise almost-complete building.

Then, in 1991, a Finnish university student posted a message that would change computing history.

[QUOTE NEEDED: Linus Torvalds's original Usenet announcement of Linux, August 1991 — "I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu)"]

Linus Torvalds released the Linux kernel — a small, functional kernel that did what GNU Hurd had been struggling to do. Torvalds hadn't set out to complete Stallman's vision. He was scratching an itch, building something for himself. But the kernel slotted into the GNU ecosystem like the last piece of a puzzle.

The result — technically GNU/Linux, though most people just say "Linux" — became the most important operating system in the world. Today it runs virtually every server on the internet, every Android phone, every one of the world's top 500 supercomputers. The open-source infrastructure that undergirds the modern digital economy — the servers, the cloud, the networks — is built overwhelmingly on the software that Stallman envisioned and that Torvalds made complete.

But it wasn't just the software that mattered. It was how the software was built.

---

Linux was developed in a way that defied everything the industry thought it knew about how complex software gets made. There was no product manager, no roadmap, no corporate hierarchy. Thousands of developers around the world contributed code, and a loose system of maintainers reviewed and integrated the contributions. It was messy, decentralized, sometimes chaotic — and it worked astonishingly well.

In 1997, Eric S. Raymond wrote an essay that tried to explain why. "The Cathedral and the Bazaar" contrasted two models of software development. The "cathedral" model was the traditional approach: a small group of architects designs the system carefully, in private, and releases it when it's ready. The "bazaar" model was what Linux demonstrated: a sprawling, open marketplace of contributions, with many hands touching the code simultaneously.

[QUOTE NEEDED: Raymond's core insight from "The Cathedral and the Bazaar" — the "given enough eyeballs, all bugs are shallow" formulation]

Raymond's argument was that the bazaar produced better results — not despite the chaos, but because of it. More contributors meant more eyes on the code, more bugs found, more perspectives applied. The essay became a manifesto, and its ideas would directly influence the next great upheaval in the movement: the 1998 moment when "free software" was rebranded as "open source" — and the ethical heart of Stallman's project was, by some accounts, surgically removed.

But before we get to that story, it's worth pausing on what Stallman actually accomplished. Not just the software — though the software changed the world. The deeper achievement was the legal and philosophical infrastructure he built around it.

---

The GNU General Public License, first released in 1989, is one of the most ingenious pieces of legal engineering in history. Stallman's problem was this: how do you use the law to guarantee freedom when the law is designed to restrict it?

His answer was copyleft — a concept so elegant it deserves to be studied in law schools alongside the great precedents. Copyleft uses copyright law against itself. Here's how it works: the GPL grants you all the freedoms Stallman defined — you can use, study, modify, and redistribute the software. But it adds one condition: any derivative work must carry the same license. If you modify GPL software and distribute it, your modifications must also be free.

This is the key move. Without copyleft, someone could take free software, improve it, and lock up the improvements. The commons would be strip-mined. With copyleft, freedom propagates. Every derivative inherits the obligation to remain free. The code can never be enclosed.

The GPL has been called a "viral" license by its critics — the freedom spreads to everything it touches. Stallman preferred a different metaphor: it's not a virus, it's an immune system. It protects the commons from enclosure.

Linux, WordPress, MediaWiki (the engine that runs Wikipedia) — all are GPL-licensed. The license has guaranteed that some of the most important software in the world remains free for anyone to use, study, and modify. It is, in a real sense, the legal backbone of the open internet.

---

By the mid-1990s, Stallman had built something remarkable: a moral philosophy, a legal framework, a community of practice, and most of an operating system. With the Linux kernel completing the picture, the free software movement had proved its central claim — that collaborative, open development could produce world-class technology.

But the movement's success attracted attention from a world that wasn't particularly interested in ethics. Corporations saw the quality of the software and wanted to use it. Investors saw the community and wanted to monetize it. Pragmatists saw the ideology and wanted to sand it down.

The question was whether "free software" could be sold to the business world without losing what made it free. In 1998, that question would be answered — and the answer would split the movement in two.

[RESEARCH NEEDED: Stallman's specific critique of how the rebranding betrayed the movement's principles. Find his most direct statement about what was lost when "free" became "open."]
