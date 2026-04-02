# Chapter 2: When Code Could Clone Itself

On February 24, 2026, Cloudflare published a blog post with a matter-of-fact title and an extraordinary claim. Steve Faulkner, an engineering manager at the company, had rebuilt Next.js — the most widely used React framework on the internet, the core product of a company valued at $9.3 billion — in under a week.

He had not done it alone, exactly. He had done it with Claude, Anthropic's AI, running through an open-source coding tool called OpenCode. Eight hundred sessions. About $1,100 in API tokens. The result was vinext, a drop-in replacement for Next.js built on top of Vite, the fast build tool created by Evan You. It implemented ninety-four percent of the Next.js API surface. It compiled up to four times faster. Its client bundles were up to fifty-seven percent smaller.

Faulkner open-sourced it under the MIT license and put it on GitHub. Cloudflare announced it had already deployed vinext in production for at least one customer.

The developer community reacted as though someone had detonated a small bomb in the middle of a dinner party. The Register ran the headline under the phrase "vibe codes." Hacker News threads accumulated hundreds of comments. The word people kept using was *unprecedented* — not because someone had built a Next.js alternative (there were dozens), but because of the economics. One person. One week. Eleven hundred dollars.

Next.js represents years of engineering by hundreds of contributors. Vercel, the company that maintains it, has raised $863 million in venture capital across six rounds, most recently a $300 million Series F in September 2025. Its entire business model depends on Next.js being the framework developers choose — the open-source project is free, and Vercel monetizes through hosting, deployment tools, and developer experience features built around it.

Cloudflare did not copy a single line of Next.js code. It did not need to. The AI read the documentation, understood the API surface, and wrote a clean implementation from scratch. The MIT license that governs Next.js was, in a legal sense, irrelevant. There was nothing to license. The code was new.

Faulkner's explanation for how this was possible contained an observation that deserves to be read slowly. "Most abstractions in software exist because humans need help," he wrote. "We couldn't hold the whole system in our heads, so we built layers to manage the complexity for us." AI does not have the same limitation. Given a specification, a solid foundation, and good guardrails, it can write everything in between. As Faulkner put it: "It's not clear yet which abstractions are truly foundational and which ones were just crutches for human cognition."

If that is true — and the vinext project suggests it is at least partially true — then the implications extend far beyond one framework. The entire software industry is built on layers of abstraction. Each layer exists because the one below it was too complex for humans to work with directly. AI does not need those layers. It can work at whatever level of abstraction the problem requires. The scaffolding that thousands of engineers spent decades constructing may be, from an AI's perspective, unnecessary.

---

This would have been a remarkable story in isolation. But it did not arrive in isolation. It arrived in a season.

Two days after Cloudflare's announcement, John O'Nolan published a newsletter that read like the confession of a man watching his life's work become obsolete. O'Nolan is the founder of Ghost, the open-source publishing platform. If you wanted to design a case study in principled open-source development, you would design Ghost.

The project started in 2013 with a Kickstarter campaign that raised nearly two hundred thousand pounds against a goal of twenty-five thousand. O'Nolan, a former WordPress core contributor, wanted to build a publishing platform that could never be captured by investors or hollowed out by misaligned incentives. So he structured Ghost as a nonprofit foundation based in Singapore. No investors. No equity. No possibility of acquisition. The code is MIT-licensed. The foundation charges for hosting but takes zero percent of creator revenue — compare that to Substack's ten percent cut. Ghost crossed $10 million in annual recurring revenue in early 2026, serving over twenty thousand paying customers.

By every measure that the open-source community uses to evaluate a project, Ghost is a triumph. It is sustainable, independent, community-governed, and mission-driven. It is the thing open source is supposed to produce.

And O'Nolan has watched, over thirteen years, what happens when you build that thing in the open.

Substack, the newsletter platform backed by hundreds of millions in venture capital, copied significant portions of Ghost's source code. This was legal. The MIT license says: do whatever you want. That is the deal. O'Nolan has never disputed the legality. But he has experienced what it feels like to build something carefully and well, to give it away on principle, and to watch a funded competitor take your work and use it to compete with you.

That experience gave his February newsletter a weight that a theorist's essay would not carry. O'Nolan was not speculating. He was reporting from the field.

---

His argument was precise and devastating. The entire framework of open-source licensing, he wrote, rests on a premise so fundamental that no one bothered to state it explicitly. Code is scarce. It is difficult to maintain. It is expensive to write. The licensing frameworks — copyleft, permissive, dual-licensing, all of them — are mechanisms for governing a scarce resource. The GPL says: if you use my scarce resource, you must share yours. The MIT license says: my scarce resource is a gift.

AI, O'Nolan argued, is overturning that premise. When code can be regenerated from a description of what it should do, the code itself is no longer the scarce artifact. The design matters. The specification matters. The understanding of the problem matters. But the implementation — the actual lines of code — is becoming a commodity.

And then the question that hung over the rest of his newsletter like smoke: if anyone can point an AI at an open-source codebase and have it rewritten from scratch, without using any of the original code, what does that mean for software licenses?

He put it more bluntly: do software licenses mean anything?

---

O'Nolan was not the first person to ask this question. Two months earlier, in December 2025, Simon Willison had demonstrated the problem at a smaller scale and with a more careful hand.

Willison is one of the most respected figures in the open-source Python community. He co-created Django, the web framework that powers Instagram, Pinterest, and thousands of other applications. He is prolific, thoughtful, and scrupulously honest about the tools he uses and the questions they raise.

In December, Willison used Codex CLI with GPT-5.2 to port a library called JustHTML from Python to JavaScript. The library is an HTML5 parser — not glamorous, but technically demanding. The kind of code that requires deep understanding of a complex specification.

The port took four and a half hours. It produced nine thousand lines of JavaScript. Forty-three commits. Nine thousand two hundred tests passing. The cost was $29.41 in API tokens — effectively free if you had a ChatGPT Plus subscription.

Willison, characteristically, did not celebrate. He asked questions. Does this library represent a legal violation of the copyright of the original? If the AI learned patterns from the Python codebase during its training, is the JavaScript output a derivative work? Where is the line between learning from code and copying it?

These were good questions. But in a follow-up post published on January 11, 2026, Willison identified something more unsettling than the legal ambiguity. The bigger problem, he argued, was not that AI could clone open-source libraries. It was that AI reduced the *demand* for them.

Consider how open-source software actually works as an ecosystem. A small team — sometimes a single person — maintains a library that solves a common problem. A date parser. A cron scheduler. A Markdown renderer. That library is used by thousands or millions of developers. The economics function because of the ratio: a handful of maintainers serve an enormous user base. Contributors emerge from the user base. Bug reports arrive. The library improves. The commons sustains itself through shared need.

Now imagine a world where every developer, instead of searching for a cron parser on npm, simply asks an AI to generate one. The AI produces a bespoke implementation in seconds. It works. It is tailored to the developer's exact requirements. There is no dependency to manage, no upstream changes to track, no maintainer to depend on.

In that world, the shared library has no users. No users means no contributors, no bug reports, no reason for the maintainer to continue. The commons does not collapse because someone attacks it. It collapses because no one needs it.

Willison pointed to Tailwind CSS as an early example. He observed that LLMs were already reducing demand for established libraries — not by competing with them directly, but by making it cheap enough to generate bespoke implementations that developers who would previously have adopted Tailwind were instead prompting their own solutions into existence. The pattern was confirmed from the other side: Tailwind's creator, Adam Wathan, reported that AI scraping had caused a forty percent drop in documentation traffic, slashing revenue by nearly eighty percent and forcing Tailwind Labs to lay off roughly three-quarters of its engineering team. The library was not being replaced by a competitor. It was being replaced by the concept of *not needing a library at all*.

This is worth pausing on, because it describes a failure mode that no one in the open-source movement anticipated.

The fear was always about exploitation — a corporation taking free code and building a proprietary empire on top of it. Amazon running open-source databases as a service without contributing back. Google using Linux to power Android while locking down its own applications. Facebook releasing React but changing the license terms to protect its patents. These were the fights that consumed the community for decades, and they were all fights about the *supply side* of the commons. Someone is taking more than they give.

Willison's observation was about the *demand side*. What if no one takes at all? What if the code sits there, perfectly available, perfectly free, and no one downloads it because they can generate their own version in thirty seconds? The library does not die from exploitation. It dies from irrelevance.

O'Nolan made the same point from a different angle. He compared the moment to what he called software's "Studio Ghibli moment" — a reference to the AI art controversy that erupted when users began generating images in Studio Ghibli's distinctive visual style. The artists of Ghibli had spent decades developing that style. The AI had not copied any specific image. It had learned the patterns — the color palettes, the composition choices, the quality of light — and produced new images that were unmistakably Ghibli without infringing on any particular work.

The parallel to code was exact. AI had not copied Ghost's code, or Next.js's code, or Willison's library. It had learned the patterns — the API surfaces, the architectural choices, the design conventions — and produced new implementations that were functionally equivalent without containing a single copied line.

In both cases, the creators were left with an uncomfortable question: if the thing you built can be replicated by studying its external characteristics, what exactly do you own?

---

If O'Nolan's essay was about the vulnerability of open source and Willison's experiment was about the erosion of shared infrastructure, there was a third development that closed the escape hatch entirely.

Geoffrey Huntley, a security researcher, had developed what he called the "z80 technique" — named after a demonstration in which he used an LLM to convert C code to assembly to specifications and then to a working Z80 Spectrum tape. The technique leverages LLMs' ability to convert between different representations of code, essentially running the model like what Huntley described as a "Bitcoin mixer for intellectual property." In one demonstration, he pointed an LLM at the compiled binary of Atlassian's ACLI Rovo Dev tool and extracted complete Python source files, system prompts, and implementation details.

This is not, in principle, new. Decompilers have existed for decades. But traditional decompilation produces output that is barely human-readable — variable names replaced with hex addresses, control flow mangled, comments stripped. The result is technically source code in the same sense that a pile of lumber is technically a house.

LLMs produce clean code. Readable. Maintainable. Documented. The barrier between compiled and source code was always more practical than theoretical — it was hard enough to reverse-engineer software that most people did not bother. LLMs removed the practical barrier. What remained was a legal question, and the legal question had no clear answer.

O'Nolan saw the implication immediately. If open-source code can be rewritten by AI without triggering copyright, and if closed-source code can be reverse-engineered by AI into readable form, then neither openness nor closure protects the logic of software. The distinction between proprietary and open source — the distinction that has organized the software industry for forty years — starts to dissolve.

Think about what that means for the companies that have built their businesses on the closed side of that distinction. Oracle charges billions of dollars a year for its database software. SAP's enterprise resource planning systems power most of the world's large corporations. Adobe's Creative Suite dominates design workflows. These companies' competitive moats are not just brand loyalty or switching costs — they are the sheer difficulty of replicating complex proprietary software from scratch.

When "from scratch" takes a week and costs eleven hundred dollars, the moat drains.

The defenders of proprietary software will argue, correctly, that a week-long AI sprint cannot replicate the full depth of a system like Oracle Database or SAP S/4HANA. Decades of edge cases, enterprise integrations, compliance certifications, and domain expertise are embedded in those codebases. But the trajectory is clear. The AI that rebuilt ninety-four percent of Next.js in February 2026 was not the most capable AI that will ever exist. It was the *least* capable AI that will ever exist for this task. Every month, the percentage climbs. Every month, the cost falls.

---

There is a temptation, at this point, to frame the situation as a crisis for open source specifically. It is not. It is a crisis for every assumption about how software is created, distributed, and maintained.

But it strikes open source with particular force, because open source made a *promise*. The promise was that if you gave your code away freely, you would receive something in return: a community of users, contributors, and co-maintainers who would collectively improve and sustain the project. The MIT license was not charity. It was a social contract. I give you my code; you give me your attention, your bug reports, your patches. The GPL made the contract explicit: if you use my code, you must share your modifications.

AI breaks both sides of that contract. On the supply side, the code can be regenerated without reference to the original — so the license never triggers. On the demand side, developers no longer need the shared library — so the community never forms.

O'Nolan, with a kind of bewildered clarity, arrived at the paradox. When Richard Stallman launched the free software movement in 1983, he was reacting to a world where software was proprietary and users were powerless. His vision was a world where all software was free to use, study, modify, and distribute. The Four Freedoms.

AI might be delivering that world. Not through licenses or legal frameworks or community norms, but through brute capability. If any software can be reconstructed from its behavior, then in practice, all software is open. All software is modifiable. All software is free — not because someone chose to free it, but because no one can keep it closed.

Stallman's vision, fulfilled by a mechanism he never imagined, through a process that destroys the institutions he built to achieve it.

O'Nolan did not pretend to have a solution. He was writing, he said, to think out loud. But the honesty of his uncertainty was more valuable than a dozen confident prescriptions. Here was a man who had staked his career on a set of principles — openness, community ownership, zero-rent extraction — and was watching those principles become insufficient to describe the world he was living in. Not wrong. Not refuted. Just... outrun. The world had changed faster than the framework could adapt.

---

There is a word for this kind of outcome in the history of political movements. It is called a Pyrrhic victory — a win so costly that it is indistinguishable from defeat. The free software movement may get everything it asked for and lose everything it built.

But that conclusion moves too fast. To understand why this paradox matters — why it is not merely an interesting theoretical observation but a genuine civilizational problem — we need to understand what the open-source movement actually built. Not just the code. The institutions. The norms. The legal frameworks. The communities. The economic engines. The thing that made it possible for a single developer to type `npm install` and receive, for free, the accumulated labor of thousands of strangers.

That infrastructure is one of the great achievements of the late twentieth century. It is also one of the least understood. Most people who use open-source software — which, at this point, means most people who use the internet — have no idea it exists. They do not know that the web server handling their request, the database storing their data, the operating system running the cloud machine, the encryption protecting their password, and the programming language the application was written in are all, in most cases, open source. They do not know that this software was written by volunteers, maintained by tiny teams, and given away for free under legal instruments that most lawyers find incomprehensible.

It was not inevitable. It was not obvious. It was built by specific people who made specific choices, starting with a programmer at MIT who was very angry about a printer and who decided that his anger was a moral argument.

His name was Richard Stallman. And the story of what he built — and why it is now in danger — begins in 1983.
