# Chapter 5: The Recursive Public

Here is a question worth sitting with: Why did some of the sharpest minds in the social sciences — anthropologists, legal theorists, political economists — spend a decade writing books about programmers sharing code?

They were not, most of them, programmers themselves. They did not care about compilers or kernel modules or the finer points of memory management. And yet, between roughly 2004 and 2012, a remarkable cluster of scholars converged on free software as an object of study with an intensity usually reserved for revolutions, religions, or financial crises. Yochai Benkler at Harvard Law. Gabriella Coleman doing fieldwork with Debian developers. Christopher Kelty following open-source communities from Boston to Berlin to Bangalore. Lawrence Lessig building Creative Commons. They saw something in the free software movement that the movement's own participants often could not see — because they were too close, too busy building, too focused on the next patch to recognize the shape of the thing they were constructing.

What the scholars saw was this: a new form of public life. Not just a better way to write software, but a fundamentally different relationship between people, tools, and power. A relationship in which communities didn't merely use technology to communicate — they built and maintained the technology itself. And in doing so, they demonstrated something political theorists had long imagined but never seen at scale: a public that governs itself by governing its own infrastructure.

This chapter is about that insight — what it means, why it matters, and whether it survives contact with artificial intelligence.

---

The clearest articulation of the idea came from an anthropologist at Rice University named Christopher Kelty.

Kelty spent years embedded in free software communities — attending conferences, lurking on mailing lists, interviewing developers in multiple countries. The result was *Two Bits: The Cultural Significance of Free Software*, published by Duke University Press in 2008 and released, in a move that embodied its own argument, under a Creative Commons license. Anyone could read it for free. Anyone could share it. The book practiced what it preached.

At the center of *Two Bits* is a concept Kelty called the "recursive public." The term sounds academic, but the idea is concrete and powerful. A recursive public, in Kelty's formulation, is "a public that is vitally concerned with the material and practical maintenance and modification of the technical, legal, practical, and conceptual means of its own existence as a public."

To understand why this matters, consider what a "public" normally means.

When political theorists talk about publics — from Jurgen Habermas's "public sphere" to Michael Warner's work on counterpublics — they describe groups of people who come together through shared discourse. The readers of a newspaper form a public. The audience of a television broadcast forms a public. The users of a social media platform form a public. In each case, the medium through which the public communicates is *given*. It exists prior to the public. The newspaper is printed by someone else. The broadcast tower is built by someone else. The algorithm is written by someone else. The public *uses* the medium but does not *control* it.

Free software communities are different. They are the first large-scale publics in history that build and maintain the medium through which they organize.

Consider the concrete case. In the 1990s, Linux developers communicated through mailing lists hosted on internet servers. They used version control systems to coordinate their code contributions. They transferred files via FTP. They debated design decisions on Usenet newsgroups. All of this ran on the internet — a global network of computers communicating through open protocols.

And what were they building? Linux — the operating system that *ran* those servers, *powered* those mailing lists, *hosted* those FTP sites. The infrastructure they depended on to collaborate was the infrastructure they were collaboratively creating. They were, in Kelty's vivid metaphor, constructing the floor they were standing on. In real time. Together.

This is what "recursive" means. The community loops back on itself. It is both the producer and the product, the builder and the building, the public and the infrastructure that sustains the public. Take away the infrastructure — take away the open protocols, the shared code, the collaborative tools — and the community that created them ceases to exist. But take away the community, and the infrastructure stops being maintained, stops being improved, eventually stops working. The two are inseparable.

---

Kelty didn't stop at the metaphor. He identified five specific practices — five components — that together constitute the recursive public. Each one emerged historically, and each one was necessary. Taken together, they describe how a movement assembles itself from the ground up.

The first practice is the most basic: sharing source code. This is the primitive act — one programmer making their work visible and available to others. It predates the free software movement by decades. The SHARE users group was doing it in 1955. Universities passed UNIX tapes around like academic papers. Before anyone theorized about openness, sharing was simply how computing worked.

The second practice is conceiving open systems — designing technologies that interoperate rather than lock users in. This is the world of standards and protocols: TCP/IP, HTTP, SMTP. The decision that the internet would be built on open protocols rather than proprietary networks was not inevitable. CompuServe, AOL, and Prodigy offered a different vision — walled gardens, each with its own rules, each owned by a corporation. The open internet won, and it won in part because the people building it believed that systems should be transparent and modifiable.

The third practice is writing copyright licenses — the legal infrastructure. Stallman's GPL, which we encountered in Chapter 3, is the paradigm case: a legal instrument that uses copyright law against itself, guaranteeing that free software cannot be enclosed. This is where the recursive public intersects with the legal system. The community doesn't just build technology; it builds the *legal framework* that protects the technology's openness.

The fourth practice is coordinating collaboration — the social technology that makes distributed work possible. Mailing lists, bug trackers, version control systems (from CVS to Subversion to Git), governance structures, codes of conduct. None of this is glamorous. Most of it is invisible to anyone outside the community. But without it, collaboration at scale is impossible. The bazaar needs a marketplace, even if nobody planned where the stalls would go.

The fifth practice is proselytizing — articulating the moral and technical vision. This is movement consciousness: not just building, but arguing for a particular way of building. Stallman's speeches, Raymond's essays, the Free Software Foundation's campaigns, the informal evangelism of developers who explain to their colleagues why open source matters. A recursive public doesn't just exist. It tells itself *why* it exists.

The five components are not a checklist to be ticked off. They are layers, each building on the ones beneath. You cannot write licenses without code to license. You cannot coordinate collaboration without open systems to collaborate through. You cannot proselytize without a story to tell — and the story is written in code, law, protocols, and shared practice. Each layer was historically contingent. Each could have gone differently. The fact that they didn't — the fact that all five assembled into a coherent whole — is what Kelty set out to explain.

---

If Kelty provided the anthropological insight — this is a new kind of public — Yochai Benkler at Harvard Law School provided the economic one. And the economic insight was, in some ways, even more radical.

Benkler's *The Wealth of Networks*, published by Yale University Press in 2006, made a claim that mainstream economists found either thrilling or preposterous: there is a third mode of production, distinct from both markets and firms.

The background: for most of the twentieth century, economists recognized two ways that complex things get made. The first is the market — decentralized, coordinated by price signals. You want a widget, someone sells a widget, the price mechanism allocates resources efficiently. The second is the firm — centralized, coordinated by hierarchy. Ronald Coase explained in 1937 that firms exist because some activities are too costly to coordinate through markets. It's cheaper to hire employees and tell them what to do than to negotiate individual contracts for every task. Markets and firms. Prices and managers. That was it. Those were the options.

Benkler saw a third option emerging: commons-based peer production. Thousands of people, most of whom had never met, were collaborating to produce Linux, Apache, and Wikipedia — software and knowledge systems that were, by any reasonable measure, world-class. They were doing this without a firm directing their work and without a market paying them to do it. No bosses. No paychecks. No business plan. And the results were extraordinary.

The title — *The Wealth of Networks* — was a deliberate echo of Adam Smith. Benkler was making an argument as fundamental as Smith's: there is a new source of productive wealth, and the existing economic categories cannot account for it. When the cost of communication drops far enough — when a programmer in Helsinki can collaborate with a programmer in Hyderabad for essentially zero transaction cost — a new coordination mechanism becomes viable. People contribute to shared projects based on intrinsic motivation, social recognition, the pleasure of craft, and the modular nature of the work. No one needs to understand the whole system. You find a bug you can fix, and you fix it. You write the documentation for the module you understand. The coordination emerges from the structure of the work itself.

This was not supposed to happen. Economists had strong theoretical reasons to believe that large-scale, complex production required either market incentives or hierarchical management. Commons-based peer production violated both assumptions and produced results that competed with — and often surpassed — the output of billion-dollar corporations. Linux was more reliable than most commercial operating systems. Apache served the majority of the world's websites. Wikipedia, for all its flaws, made the Encyclopedia Britannica obsolete.

Benkler's prediction — that commons-based peer production would expand beyond software — proved remarkably accurate. OpenStreetMap applied the model to cartography. Arduino and RISC-V applied it to hardware. Kickstarter and crowdfunding platforms applied the logic of distributed contribution to capital formation. Citizen science projects applied it to research. The model worked wherever the work could be modularized and the communication costs were low enough.

But Benkler was, with hindsight, too optimistic about where the wealth would land. The "wealth of networks" — the value created by commons-based peer production — accrued disproportionately not to the contributors but to the platforms that aggregated their work. Google built a search empire on the open web that peers had created. Facebook built a social empire on the content that users generated. Amazon built a cloud empire on the open-source databases that communities maintained. The producers and the profiteers were not the same people. This was a problem that Benkler's framework acknowledged but underestimated — and it would become the central tension of the open-source business model explored in Chapters 7 and 8.

---

While Benkler saw economics, Gabriella Coleman saw politics.

Coleman's *Coding Freedom: The Ethics and Aesthetics of Hacking*, published by Princeton University Press in 2012, was based on years of ethnographic fieldwork with the Debian Linux community. Debian is a fascinating case precisely because it has no corporate sponsor. Unlike Red Hat (backed by IBM), Ubuntu (backed by Canonical), or Android (backed by Google), Debian is run entirely by volunteers. It has its own constitution. Its own social contract. Elaborate voting procedures for leadership positions. Formal processes for resolving disputes about which software packages to include.

Coleman's insight was that Debian's governance structures — and hacker culture more broadly — represent a working instantiation of liberal political philosophy. Not liberal in the American partisan sense, but liberal in the tradition running from John Locke through John Stuart Mill: a political framework centered on individual autonomy, free expression, transparency, and governance by consent.

Hackers, Coleman observed, generally do not think of themselves as political actors. They think of themselves as engineers solving problems. But their practices are saturated with political commitments. The insistence on transparency — that code should be readable, that decisions should be made on public mailing lists, that authority should derive from demonstrated competence rather than title or tenure — these are not merely technical preferences. They are political principles, expressed through a technical medium.

The tension Coleman identified is revealing. Hackers are ferociously anti-authoritarian — they resist corporate control, government surveillance, and institutional gatekeeping. And yet they build elaborate systems of authority: maintainer hierarchies, code review processes, licensing regimes, constitutional governance structures. They reject the authority of firms and states while constructing their own forms of legitimate authority from scratch. This is not a contradiction. It is the fundamental project of liberal democracy, played out in a new arena: How do you organize collective action while preserving individual freedom? How do you coordinate without coercing?

The Debian community's answer — rough consensus, transparent debate, meritocratic authority, formalized rights — would be instantly recognizable to any student of democratic theory. What makes it novel is the medium. These principles are not inscribed in parchment or argued in legislatures. They are embedded in code, licenses, mailing list archives, and version control histories. The political philosophy is practiced, not preached. Coleman's contribution was to make visible what the practitioners themselves often could not see: that they were doing political theory with their keyboards.

---

Kelty, Benkler, and Coleman wrote during what might be called the heroic phase of open source — the period of building, expanding, winning. By the time Nadia Eghbal published *Working in Public* with Stripe Press in 2020, the heroic phase was over. The infrastructure had been built. Now it needed maintenance. And maintenance, it turned out, looked nothing like the scholars' optimistic models.

Eghbal's central observation is devastating in its simplicity. The romantic image of open source — Raymond's "bazaar," Benkler's "commons-based peer production," the vision of thousands of contributors collaborating joyfully — describes a tiny minority of projects. The vast majority of open-source software is not a bazaar. It is a stadium.

In a stadium, there is a performer — one person, maybe two — and a massive audience. The audience watches. The audience benefits. The audience does not contribute. The performer does all the work. And as the audience grows, the performer's burden increases: more bug reports, more feature requests, more questions, more pull requests to review, more emails to answer. The communication overhead scales linearly with users and eventually overwhelms the maintainer's capacity.

This is the reality of most popular open-source software. The NPM packages that the entire JavaScript ecosystem depends on. The Python libraries that power machine learning research. The small, critical utilities — compression tools, logging frameworks, cryptographic libraries — that sit at the foundation of the internet's infrastructure. These are often maintained by a single person, in their spare time, for free.

The consequences of this maintenance crisis have been severe. In December 2021, a critical vulnerability was discovered in Log4j, a Java logging library used by virtually every major technology company. The library was maintained by Apache's Logging Services team — sixteen unpaid volunteers distributed across the globe, with no dedicated security resources. In 2014, the Heartbleed vulnerability in OpenSSL — the encryption library protecting most internet traffic — revealed that this foundational security infrastructure was maintained by a skeleton crew — one full-time developer, Stephen Henson, and three part-time volunteers, surviving on roughly two thousand dollars a year in donations. In 2024, a sophisticated social engineering attack targeted xz utils, a compression library embedded deep in Linux systems. An attacker using the pseudonym Jia Tan spent over two years — from late 2021 to early 2024 — building trust with the project's sole maintainer, using sock puppet accounts to pressure the overwhelmed developer into granting co-maintainer access. Once in position, Jia Tan inserted a backdoor into versions 5.6.0 and 5.6.1, scoring a perfect 10.0 on the Common Vulnerabilities and Exposures severity scale. The attack was discovered by software developer Andres Freund on March 29, 2024 — by chance, before the compromised versions reached most production systems.

Eghbal had anticipated this dynamic in her 2016 Ford Foundation report, *Roads and Bridges*, where she argued that open-source software is public infrastructure — comparable to roads, bridges, and water systems — and that, like physical infrastructure, it requires sustained investment in maintenance. The analogy is precise. No one glamorizes bridge maintenance. No one writes books about the heroism of repaving highways. But when the bridge collapses, everyone notices.

What Eghbal's work reveals, when set against the earlier scholarship, is a paradox at the heart of the recursive public. Kelty argued that free software communities build and maintain their own infrastructure. But what happens when the "community" is actually one person? What happens when the recursive public collapses into a recursive individual — a single maintainer who is simultaneously the builder, the user, the governance structure, and the sole point of failure? The recursion doesn't disappear. It just becomes unsustainable.

---

Between roughly 2004 and 2012, then, four distinct disciplines converged on the same phenomenon and saw four different things.

An anthropologist saw a new form of public life — a community that builds its own conditions of existence. A legal economist saw a new mode of production — neither market nor state, but something the textbooks hadn't imagined. A political anthropologist saw liberal philosophy in practice — freedom, transparency, and consent expressed through code rather than constitutions. And a researcher at the Ford Foundation saw infrastructure — public goods being maintained, badly, by unpaid volunteers.

They were all right. And the fact that they were all right — that the same phenomenon could sustain four distinct and valid interpretations — suggests the depth of what was actually happening. Free software was not just a technical methodology or a business strategy. It was a social experiment of extraordinary ambition: a demonstration that communities could build, govern, and maintain complex systems without the coordination mechanisms of markets or states.

The question is whether the experiment scales to the next frontier.

---

There is a reason this book lingers on the recursive public before moving to the AI chapters. The concept contains a test — a way of asking whether any given "open" initiative is genuinely open or merely performing openness.

Kelty identified two core properties that a recursive public must possess: availability and modifiability. Availability means transparency — you can see it, inspect it, read it. Modifiability means you can change it — not just look under the hood, but rebuild the engine.

Both properties were present in classic open-source software. The source code was available — anyone could read it. And the source code was modifiable — anyone with sufficient skill could change it, improve it, fork it, and redistribute the result. The barrier to entry was knowledge, not capital. A talented programmer with a $500 laptop could contribute to Linux. The recursive public was accessible because the technology was accessible.

Now consider AI.

Availability, in a limited sense, exists. Meta has released the weights for its Llama models. Mistral, Alibaba, and DeepSeek have released weights for theirs. You can download these models. You can run them. You can inspect the architecture. In that narrow sense, the models are "available."

But modifiability is where the framework breaks down. To truly modify an AI model — to retrain it, to change its behavior at a fundamental level, to understand *why* it produces the outputs it does — requires resources that no community of volunteers can assemble. Training a frontier model costs tens or hundreds of millions of dollars. It requires proprietary datasets that are not released even when the weights are. It requires specialized hardware — clusters of GPUs or TPUs — that only a handful of organizations in the world possess.

You can fine-tune a model, yes. You can adjust its behavior at the margins through techniques like RLHF or LoRA adapters. But this is modification in the way that repainting a house is modification. The structure — the foundation, the framing, the plumbing — remains the product of whoever trained the model. And that "whoever" is invariably a corporation with billions of dollars in capital.

Kelty's recursive public depends on a community that can "maintain and modify the technical, legal, practical, and conceptual means of its own existence." Can there be such a community for AI? Can there be a public that builds and maintains the infrastructure of artificial intelligence — not just uses it, not just fine-tunes it, but genuinely controls the conditions of its own technological existence?

The honest answer, as of 2026, is: not yet. And possibly not ever — at least not for frontier AI systems. The economics are too concentrated. The compute is too expensive. The knowledge required to train a model from scratch is too specialized and too dependent on resources that only a few institutions control.

This is a structural break from everything the open-source movement has known. Software was democratic in a way that AI is not. A compiler can be built by a community. A foundation model cannot — not at the frontier, not without the resources of a Google or a Meta or an OpenAI. The recursive loop that Kelty described — the community building the infrastructure it depends on — may not close for AI. The community may remain, permanently, a user of infrastructure it does not and cannot control.

If that is true, it changes everything about the politics of openness. The question is no longer whether to share the code. It is whether sharing the code is even meaningful when the thing that matters — the trained model, the dataset, the compute infrastructure — remains firmly in the hands of a few.

---

But there is an alternative reading, and it would be a mistake to close this chapter without it.

Perhaps the recursive public for AI is not a group of developers training models. Perhaps it is something else entirely — a community that builds and maintains the governance infrastructure around AI. The safety evaluation frameworks. The alignment research. The red-teaming practices. The legal standards for responsible deployment. The institutions that decide what AI systems should and should not do.

This is what Anthropic's structure hints at — and what Chapter 10 will explore in detail. The company's Constitutional AI methodology, its commitment to interpretability research, its refusal to deploy Claude for mass surveillance or autonomous weapons: these are attempts to build governance infrastructure for a technology that is too powerful and too concentrated to be governed by the old recursive model of shared code.

The recursive public may not be dead. It may be evolving. The recursion may shift from "we build the code together" to "we build the rules together." Whether that shift is sufficient — whether governance without control is meaningful in a world where the technology itself is controlled by a few — is the question the rest of this book will try to answer.

One of Kelty's five components was writing copyright licenses — the legal infrastructure that protected openness. That component is now under unprecedented strain. The licenses designed for software — GPL, MIT, Apache — were built for a world where the thing being licensed was code: readable, reproducible, modifiable by anyone with skill. AI models are none of those things in the same way. The legal infrastructure of openness is cracking under the weight of a technology it was never designed to bear.

That story — the license wars, old and new — is where we turn next.

*A note on the scholars.* Kelty is now a professor at UCLA with joint appointments in the Institute for Society and Genetics, Information Studies, and Anthropology. His post-*Two Bits* work shifted toward the broader problem of participation — culminating in *The Participant* (University of Chicago Press, 2019), an historical ethnography of the concept and practice of participation across domains from free software to citizen journalism to science. He has not, as of early 2026, published a sustained treatment of AI through the recursive public lens, though the framework he built is precisely the one this chapter applies. Benkler remains at Harvard Law School as the Berkman Professor of Entrepreneurial Legal Studies. His recent work has focused on political economy, propaganda, and disinformation rather than updating the commons-based peer production framework for AI specifically. Coleman is the Ernest E. Monrad Professor of the Social Sciences in the Department of Anthropology at Harvard, with a faculty affiliation at the Berkman Klein Center for Internet and Society. She is currently finishing a book of essays based on her 2022 Lewis Henry Morgan Lectures and co-authoring work on how hackers professionalized between the 1990s and 2000s — still focused on hacker culture, but not yet directly engaging AI governance. The scholarly apparatus built between 2004 and 2012 remains the most robust framework available for understanding what "open" means. That none of its architects has yet turned it fully toward AI is itself a data point worth noting.
