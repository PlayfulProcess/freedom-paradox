# Chapter 3: Free as in Freedom

The previous chapter ended with a programmer at MIT who was very angry about a printer. It is time to meet the anger — and the extraordinary thing it built.

Before there was a movement, there was a culture. And before there was a culture war, the culture was so uniform that no one bothered to name it. In the 1950s, 1960s, and well into the 1970s, sharing software was not an ideology. It was simply how computing worked — the way sharing recipes is how cooking works, or sharing case law is how the legal profession works. The notion that someone would write a useful program and then prevent other people from reading, modifying, or learning from it would have struck most programmers of that era as bizarre. Like a mathematician publishing a theorem but refusing to show the proof.

The SHARE users group — its name says everything — was founded in 1955 by users of IBM's 704 mainframe. It began distributing free software that same year, making it one of the oldest collaborative institutions in computing history. SHARE was not a radical organization. It was a practical one. IBM's machines were expensive. The software that ran on them was primitive. If you wrote a sorting algorithm that worked, why wouldn't you share it? Your colleague down the hall needed one too. The cost of sharing was zero. The benefit was mutual.

This logic scaled naturally. Universities passed code around like academic papers — which, in a sense, they were. When Ken Thompson designed the first UNIX operating system at Bell Labs in the late 1960s, it was distributed freely to universities and research labs worldwide. Students studied it. Professors modified it. Entire computer science curricula were built around reading and annotating UNIX source code. John Lions's *Commentary on UNIX 6th Edition*, written in 1977, became what is commonly held to be the most photocopied book in computer science — a samizdat textbook, passed from hand to hand for nearly two decades. When the license for the 7th Edition of UNIX specifically excluded classroom use of the source code, the Commentary could no longer be taught legally. Students met after hours to discuss it. Fifth-generation photocopies became prized possessions among Unix kernel hackers. It was not formally published until 1996, when the Santa Cruz Operation finally authorized the release of the twenty-year-old source code.

This was not idealism. Nobody at SHARE was making a political statement. Nobody distributing UNIX tapes thought of themselves as a freedom fighter. The openness was structural: software came bundled with hardware, and the hardware was where the money was. IBM did not sell software. IBM sold machines. The software was a means to an end — a way to make the machine useful. Giving it away was not generosity. It was common sense.

Then the economics changed, and the lawyers arrived.

---

A series of legal decisions in the late 1970s and early 1980s established that software could be copyrighted — that it was, in legal terms, a creative work comparable to a novel or a song, not a mathematical procedure that belonged to everyone. Bell Labs copyrighted UNIX in 1979. Non-disclosure agreements proliferated. Proprietary licenses became standard. The best programmers were recruited out of universities into corporate shops where their work was locked behind legal walls.

What had been the default — sharing — became the exception. What had been the exception — restriction — became the default. And the speed of the reversal was astonishing. In the space of a decade, the culture of computing flipped. A generation of programmers who had learned their craft by reading other people's code suddenly found that other people's code was off-limits.

Richard Stallman was at the center of this reversal, and he felt it with a clarity that bordered on rage.

Stallman was a programmer at MIT's Artificial Intelligence Laboratory — one of the most creative computing environments on Earth. The AI Lab ran on a culture of radical openness. If a program broke, you fixed it. If someone wrote something useful, they shared it. Source code circulated freely, because knowledge shared is knowledge multiplied.

Then the lab got a new printer. A Xerox machine. It jammed constantly, and in the old culture, that wouldn't have been a problem — someone would simply look at the source code for the printer driver, find the bug, and fix it. Stallman had done exactly this with a previous printer, adding code that alerted users when their print jobs were done or when paper was jammed. A small hack. A shared improvement. The way things worked.

But the Xerox printer came with a catch. Its software was proprietary. The source code was locked. When Stallman asked a researcher at Carnegie Mellon for a copy — someone who had recently come from Xerox PARC and was still working on the laser printer — the researcher refused. He had signed a non-disclosure agreement with Xerox.

For Stallman, this was not a professional inconvenience. It was a moral catastrophe. The NDA was a contract that compelled the signer to act selfishly — to withhold useful information from the community. Software was supposed to be a tool to serve people; that was why Stallman and his labmates spent their time writing it. And yet, through a combination of greed and legal restriction, people were forced to suffer because they were prevented from improving the tools they depended on. The moment crystallized everything Stallman had been sensing about the changing culture of computing: the industry was shifting from shared scientific inquiry to proprietary control, where users were prohibited from understanding or modifying the tools they relied upon.

This was not an isolated incident. It was a symptom. All around Stallman, the AI Lab was being hollowed out. The best hackers were being hired away by Symbolics and other companies, taking their skills into closed environments. The community that had sustained the lab's culture was dissolving. Stallman saw, with painful precision, what was being lost — not just convenience, but a way of life. A way of relating to technology that treated the user as a peer, not a consumer. A world where you could look under the hood of any machine you used and understand, modify, or improve it.

He refused to accept it. In 1983, he announced the GNU Project: an audacious effort to build a complete, free operating system from scratch. Not free as in price — free as in freedom. The distinction would define everything that followed.

---

In early 1985, Stallman published "The GNU Manifesto" — a document that reads less like a technical specification and more like a political declaration. It appeared in Dr. Dobb's Journal, a magazine for working programmers, but its arguments were moral, not commercial. "So that I can continue to use computers without dishonor," Stallman wrote, "I have decided to put together a sufficient body of free software so that I will be able to get along without any software that is not free." Software, Stallman insisted, is a form of knowledge. Restricting access to it harms everyone — not just the people who want to use it, but the entire ecosystem of innovation that depends on the free flow of ideas. The Manifesto laid a philosophical foundation for the project, arguing that proprietary licenses foster division among programmers and users by prohibiting sharing and collaboration.

The Manifesto's claims were radical, and they were meant to be. Stallman argued that proprietary software was not merely inconvenient but ethically wrong — that a programmer who prevents users from sharing and modifying a program is acting against the common good. He anticipated the counterarguments with a debater's precision. What about programmers' livelihoods? They can find other business models — consulting, custom development, teaching. What about the incentive to innovate? The history of software showed that the most innovative work happened when code was shared, not when it was locked up. What about the rights of creators? The rights of users matter too, and the social cost of restriction outweighs the private benefit of control.

These were not hypothetical arguments. Stallman was staking his career on them. He had left his position at MIT (while keeping office access) to work on GNU full-time, forgoing a comfortable academic career for an uncertain mission. The Manifesto was his public commitment — a line drawn in the sand.

That same year, he founded the Free Software Foundation. And at the foundation's core he placed four principles — the Four Freedoms — that would become the ethical bedrock of the entire movement:

**Freedom 0:** The freedom to run the program for any purpose.

**Freedom 1:** The freedom to study how the program works and modify it.

**Freedom 2:** The freedom to redistribute copies.

**Freedom 3:** The freedom to distribute copies of your modified versions.

Read these carefully. They are not suggestions for good business practice. They are claims about what humans are *owed* in their relationship to the tools they use. Stallman wasn't arguing that free software made better products or bigger profits. He was arguing that restricting software is ethically wrong — a violation of the user's autonomy. Freedom 1 requires access to the source code. Freedom 3 requires the right to share your improvements. Together, they define a relationship between user and technology that is fundamentally different from the consumer model: the user is not a passive recipient but an active participant, with both the right and the ability to understand and shape the tools they depend on.

This moral framing would later be deliberately discarded by the "open source" rebranding of 1998 — a story for the next chapter. But the framing matters enormously for the question this book is ultimately asking. Because the Four Freedoms contain an assumption so deep it was invisible in 1985: the thing being freed is benign.

A text editor is benign. A compiler is benign. An operating system is benign. When Stallman wrote Freedom 0 — "to run the program for any purpose" — the "any purpose" was limited by the nature of what software could do. A text editor edits text. A compiler compiles code. The range of purposes is bounded by the tool's capabilities, and those capabilities are narrow, specific, and well-understood. Nobody was going to use Emacs for mass surveillance. Nobody was going to deploy GCC as an autonomous weapon.

Now consider an AI system that can write code, generate disinformation, design pathogens, or conduct cyberattacks. "Any purpose" takes on a different character entirely. Freedom 0 — run the program for any purpose — becomes a statement not about autonomy but about risk. Freedom 2 — redistribute copies — becomes a question about proliferation. Freedom 3 — distribute modified versions — becomes a question about whether someone can fine-tune a powerful model to remove its safety guardrails and hand it to anyone on Earth.

The question this book will return to, again and again, is what happens when the Four Freedoms meet a technology where "any purpose" includes purposes that could destabilize civilization. Stallman's framework was built for a world of tools. It may not survive a world of agents.

But in 1985, that question was forty years away. First, Stallman had an operating system to build.

---

The GNU Project was an extraordinary act of construction. Stallman and a growing community of contributors built the tools of a complete operating system, piece by piece. GCC — the GNU Compiler Collection — became the standard compiler for the computing world. Emacs became one of the most powerful text editors ever created. GNU Coreutils, the shell, the libraries — component after component, they built it all.

But they needed one more thing. The most critical piece of any operating system: the kernel, the core program that manages hardware resources and allows everything else to run. The GNU Project's kernel — called GNU Hurd — proved fiendishly difficult to complete. Its ambitious microkernel architecture turned out to be far harder to implement than anyone had anticipated. For years, it was the missing foundation of an otherwise almost-complete building.

Then, in August 1991, a twenty-one-year-old Finnish university student posted a message to the comp.os.minix Usenet newsgroup. Linus Torvalds was writing a small operating system kernel as a hobby project — something to learn about the 386 processor in his new PC. His message was almost comically modest: "I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones," he wrote. He mentioned he had ported bash and gcc, and things seemed to work. The project had been brewing since April.

Torvalds released the Linux kernel under the GPL. It was a small, functional kernel that did what GNU Hurd had been struggling to do. Torvalds hadn't set out to complete Stallman's vision. He was scratching an itch, building something for himself. But the kernel slotted into the GNU ecosystem like the last piece of a puzzle.

The result — technically GNU/Linux, though most people just say "Linux" — became the most important operating system in the world. Today it runs virtually every server on the internet, every Android phone, every one of the world's top 500 supercomputers. The open-source infrastructure that undergirds the modern digital economy — the servers, the cloud, the networks — is built overwhelmingly on the software that Stallman envisioned and that Torvalds made complete.

But it wasn't just the software that mattered. It was how the software was built.

---

Linux was developed in a way that defied everything the industry thought it knew about how complex software gets made. There was no product manager, no roadmap, no corporate hierarchy. Thousands of developers around the world contributed code, and a loose system of maintainers reviewed and integrated the contributions. It was messy, decentralized, sometimes chaotic — and it worked astonishingly well.

Conventional wisdom in software engineering held that this should have been impossible. Fred Brooks, in his classic 1975 work *The Mythical Man-Month*, had articulated what seemed like an iron law: adding more people to a late software project makes it later. Coordination costs grow faster than productivity. Large teams produce tangled, buggy code. The best software comes from small, tightly managed groups.

Linux violated every element of this model and produced an operating system that was more reliable, more secure, and more rapidly improving than most commercial alternatives. How?

In 1997, Eric S. Raymond wrote an essay that tried to explain why. "The Cathedral and the Bazaar" contrasted two models of software development. The "cathedral" model was the traditional approach: a small group of architects designs the system carefully, in private, and releases it when it's ready — like building a medieval cathedral, with master builders who control every detail. The "bazaar" model was what Linux demonstrated: a sprawling, open marketplace of contributions, where the design emerges from the interactions of many independent actors.

Raymond distilled the bazaar's advantage into a principle he called "Linus's Law": given enough eyeballs, all bugs are shallow. The idea is deceptively simple. If thousands of people are reading the code, every bug is likely to be obvious to at least one of them. What is an impenetrable mystery to the original developer may be a familiar pattern to contributor number 437. The sheer diversity of perspectives — different backgrounds, different expertise, different ways of thinking about problems — creates a collective intelligence that no cathedral team can match.

This was not just an observation about debugging. It was a claim about organizational design. The bazaar model worked because it lowered the cost of participation to nearly zero. You didn't need to be hired, vetted, or trained. You didn't need to understand the entire system. You just needed to find one bug, fix it, and submit the fix. The maintainers — Torvalds and a trusted circle of lieutenants — handled integration. The contributors handled discovery. The division of labor was elegant precisely because it was unplanned.

Raymond's essay became a manifesto in its own right, and its ideas would directly influence the next great upheaval in the movement: the 1998 moment when "free software" was rebranded as "open source" — and the ethical heart of Stallman's project was, by some accounts, surgically removed. That story belongs to Chapter 4.

But there is a deeper point here that connects forward to Chapter 5 and Christopher Kelty's concept of the "recursive public." Linux was not just a piece of software built by a new method. It was a *community* that built and maintained the very infrastructure it depended on. The developers who contributed to Linux were using the internet to collaborate — and Linux *was* the internet's infrastructure. The mailing lists, the version control systems, the servers hosting the code — all of it ran on the software the community was building. They were constructing the floor they were standing on, in real time, together. That recursive quality — the community that builds its own conditions of existence — is what makes open source more than a development methodology. It is, as Kelty would later argue, a new form of public life.

But before we get to that story, it's worth pausing on what Stallman actually accomplished. Not just the software — though the software changed the world. The deeper achievement was the legal and philosophical infrastructure he built around it.

---

The GNU General Public License, first released in 1989, is one of the most ingenious pieces of legal engineering in history. Stallman's problem was this: how do you use the law to guarantee freedom when the law is designed to restrict it?

Copyright law gives creators the exclusive right to control how their work is copied, modified, and distributed. It is, by design, a tool of restriction. Stallman needed a tool of liberation. He could have simply disclaimed his copyright — placed GNU software in the public domain, where anyone could do anything with it. But he saw the trap in that approach. If the software were in the public domain, a corporation could take it, improve it, and release the improved version under a proprietary license. The commons would be strip-mined. The free software would be used as raw material for unfree software.

His answer was copyleft — a concept so elegant it deserves to be studied in law schools alongside the great precedents. Copyleft uses copyright law against itself. Here's how it works: the GPL grants you all the freedoms Stallman defined — you can use, study, modify, and redistribute the software. But it adds one condition: any derivative work must carry the same license. If you modify GPL software and distribute it, your modifications must also be free.

Think of it this way. Imagine a public park with a rule: anyone can use this park, anyone can add to it, anyone can plant new gardens or build new paths. But if you build something in this park, it becomes part of the park. You cannot fence off your addition and charge admission. Your improvement inherits the same openness that let you build it in the first place. The park can grow forever, but it can never shrink. No one can enclose what has been made common.

This is the key move. Without copyleft, someone could take free software, improve it, and lock up the improvements. Freedom would be a one-way valve — flowing out of the commons and into proprietary products. With copyleft, freedom propagates. Every derivative inherits the obligation to remain free. The code can never be enclosed. The commons has an immune system.

The GPL has been called a "viral" license by its critics — the freedom spreads to everything it touches. Stallman preferred the immune system metaphor, and it is more accurate. A virus is indiscriminate and harmful. An immune system protects a living body from enclosure and extraction. The GPL does not spread freedom randomly. It ensures that freedom, once granted, cannot be revoked.

Linux, WordPress, MediaWiki (the engine that runs Wikipedia) — all are GPL-licensed. The license has guaranteed that some of the most important software in the world remains free for anyone to use, study, and modify. It is, in a real sense, the legal backbone of the open internet.

---

By the mid-1990s, Stallman had built something remarkable: a moral philosophy, a legal framework, a community of practice, and most of an operating system. With the Linux kernel completing the picture, the free software movement had proved its central claim — that collaborative, open development could produce world-class technology.

But the movement's success attracted attention from a world that wasn't particularly interested in ethics. Corporations saw the quality of the software and wanted to use it. Investors saw the community and wanted to monetize it. Pragmatists saw the ideology and wanted to sand it down.

The word "free" was the problem — or rather, the word was the excuse. In English, "free" is ambiguous. Free as in freedom, or free as in free beer? Stallman had been explaining the distinction for a decade, but to a business audience, the word conjured images of zero revenue. Worse, the moral framework felt aggressive — it called proprietary software unethical, which was an uncomfortable thing to hear if you worked at Microsoft or Oracle.

The question was whether "free software" could be sold to the business world without losing what made it free. In 1998, that question would be answered — and the answer would split the movement in two.

Stallman has articulated his critique of the rebranding with remarkable consistency for nearly three decades, most fully in his essay "Why Open Source Misses the Point of Free Software." His most direct formulation: "Open source is a development methodology; free software is a social movement." The two terms, he has written, describe almost the same category of software, but they stand for views based on fundamentally different values. The free software movement campaigns for freedom as a matter of justice. The open source movement values mainly practical advantage and does not campaign for principles. What was lost, in Stallman's view, was precisely the thing that made the movement a movement rather than a methodology — the insistence that restricting software is ethically wrong, not merely inefficient.
