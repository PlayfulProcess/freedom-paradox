# Chapter 6: The License Wars

On August 10, 2023, Armon Dadgar and Mitchell Hashimoto — co-founders of HashiCorp, one of the most influential infrastructure companies in the open-source world — published a blog post announcing that every major product in their portfolio was switching licenses. Terraform, Vault, Consul, Nomad — the tools that thousands of companies used to provision and manage cloud infrastructure — would move from the Mozilla Public License, a permissive open-source license, to the Business Source License. Effective immediately.

The BSL is not open source. It is "source-available" — you can read the code, modify it for internal use, even contribute to it. But you cannot offer HashiCorp's software as a hosted commercial service without a separate commercial agreement. The change was aimed at one class of user: cloud providers who took HashiCorp's open-source tools and offered them as managed services, capturing the revenue that HashiCorp believed should have been theirs.

[QUOTE NEEDED: Dadgar's exact language from the August 10 announcement on why they made the switch]

Five days later, on August 15, a group of developers and companies published the OpenTF Manifesto — an open letter demanding that HashiCorp reverse the license change or relinquish the project to a foundation. Within weeks, the manifesto's GitHub repository had accumulated over 33,000 stars. Roughly 140 companies and 700 individuals pledged their support. The language was blunt: HashiCorp had betrayed a social contract.

By September 20, the Linux Foundation had accepted the fork. OpenTF was renamed OpenTofu. By January 2024, it had shipped its first stable release. The Cloud Native Computing Foundation, which required all tools in its ecosystem to be fully open source, could no longer use Terraform. HashiCorp's product was alive and well — but so was a community-owned alternative that would develop independently, forever.

In February 2025, IBM completed its acquisition of HashiCorp for $6.4 billion at thirty-five dollars per share — a deal announced in April 2024.

Thirty-three thousand stars on a document about software licensing. That number deserves a moment of attention. These were not casual clicks. Each star was a developer registering a position — publicly, under their real GitHub identity — on a question that most people would find staggeringly boring. What license should a piece of infrastructure software carry?

The answer to why they cared is the subject of this chapter. Licenses are not paperwork. They are philosophy made enforceable. They are the legal code that encodes what a community believes about freedom, reciprocity, and who gets to profit from shared work. And in 2023 and 2024, that legal code became a battlefield.

---

The previous chapter ended with Kelty's observation that writing copyright licenses is one of the five essential practices of a recursive public — a community that builds and maintains the infrastructure of its own existence. This chapter is the story of that practice under strain. The licenses designed for a world of shared code are cracking under the weight of a world where shared code generates billions of dollars in revenue for companies that didn't write it.

But before the wars, the weapons. A brief tour of the arsenal.

---

Every open-source license occupies a point on a spectrum. On one end: maximum freedom for the user of the code, including the freedom to close it. On the other end: maximum guarantee that the code stays free, even if that limits what you can do with it. The spectrum maps, with uncanny precision, onto the philosophical split between Stallman's free software movement and the 1998 open-source rebranding.

The MIT License is the world's most popular. It says, in roughly thirty words of legal text: do whatever you want with this code. Use it commercially. Modify it. Distribute it. Sell it. Close it. Wrap it in a proprietary product. The only obligation is to keep the copyright notice. That's it.

React, the library that powers much of the modern web, is MIT-licensed. So are Node.js, jQuery, VS Code, Next.js, Ghost, Ruby on Rails, and .NET. The MIT License is the default choice of the JavaScript ecosystem, the startup world, and any project that prioritizes adoption above all else. It is the legal expression of the 1998 pragmatists' bet: if we remove every barrier to use, adoption will be so massive that the benefits of the ecosystem will outweigh whatever we lose to free-riders.

The Apache License 2.0 is MIT's corporate cousin. It grants the same broad permissions but adds two provisions that matter at enterprise scale: an explicit patent grant (users receive a license to any patents the contributors hold that cover the code) and a patent retaliation clause (if you sue the project over patents, your license is terminated). Google, Microsoft, and Amazon favor Apache for their open-source releases — Kubernetes, TensorFlow, and Android's core are all Apache-licensed. The patent provisions give legal certainty to companies deploying the code in products that touch billions of users.

The BSD licenses — two-clause and three-clause variants — are functionally similar to MIT, with a heritage in academic and research computing. Their most consequential deployment: Apple built macOS and iOS on top of FreeBSD components and the Mach kernel. This was possible because BSD's permissive terms allowed Apple to take the code, modify it extensively, and release the result as proprietary software. Under the GPL, this would have been illegal. Under BSD, it was the entire point.

---

On the other end of the spectrum sits the GNU General Public License — Stallman's masterwork, encountered in Chapter 3. The GPL grants all the same freedoms as MIT: use, study, modify, distribute. But it adds one condition that changes everything. Any derivative work must carry the same license. If you modify GPL code and distribute it, your modifications must also be open, under the GPL, with source code available.

This is copyleft. Freedom that propagates. The park that can grow forever but never shrink.

The GPL is the license of Linux, WordPress, MediaWiki. It is the legal backbone of the open internet's infrastructure. And it is, by design, inconvenient. It deliberately constrains what you can do with the code — not to restrict freedom, but to guarantee it. Stallman understood that without enforcement, openness is a one-way valve. Code flows out of the commons into proprietary products, and nothing flows back. The GPL is the mechanism that prevents this drain. The immune system that protects the commons from enclosure.

But the GPL has a hole. A hole that would eventually blow the license wars wide open.

The GPL's obligations trigger on *distribution*. When you distribute a modified version of GPL code — ship it in a product, publish it on a website for download — you must include the source code under the GPL. But what happens when you don't distribute the software at all? What happens when you run it on your own servers, and users interact with it over the internet?

Nothing. The GPL doesn't trigger. You can take a GPL database, modify it extensively, run it as a cloud service, charge customers for access, and never release a line of your modified source code. The users never receive a copy of the software. They receive a *service* powered by the software. And distribution of a service is not distribution of the software.

This is the SaaS loophole. And in a world where software increasingly runs in the cloud — where "using" a program means connecting to someone else's server — the loophole swallowed the rule.

The AGPL, the Affero General Public License, was written to close it. AGPL extends the GPL's obligations to network interaction: if users interact with AGPL software over a network, that counts as distribution, and the source code obligations apply. It is the GPL updated for the cloud era. MongoDB originally used AGPL. Grafana uses it. Nextcloud uses it. But the AGPL arrived too late and too aggressively for many companies — Google, Apple, and others have internal policies flatly prohibiting AGPL code in their products, treating it as legally radioactive.

And then there is the LGPL — the Lesser General Public License — which allows proprietary software to *link to* LGPL libraries without the copyleft triggering for the proprietary code. It was designed for libraries where the goal is maximum adoption: glibc, parts of Qt, portions of FFmpeg. Stallman originally called it the "Library" GPL, then renamed it "Lesser" — to discourage its overuse, to signal that it was a compromise, not a preference.

---

If you find license taxonomy dry, you are not alone. Most developers do. But the taxonomy encodes a forty-year argument about the nature of software freedom, and the choices embedded in it have consequences worth billions of dollars. Consider two paths.

Path one: you build a database and license it under MIT. You get maximum adoption. Every cloud provider on Earth can offer your database as a managed service. They bear the operational cost and capture the hosting revenue. Your user base is enormous, your community vibrant, your brand ubiquitous. You are the standard. You are also, unless you find another business model, broke.

Path two: you build a database and license it under the GPL. Corporate adoption is slower — legal departments flag the copyleft, engineers look for permissive alternatives. But anyone who distributes a modified version must release the source. Your code cannot be enclosed. Your commons has an immune system. Except: the biggest users of your database — the cloud providers running it as a service — never distribute it at all. The SaaS loophole means the GPL's protections don't reach the companies extracting the most value.

Neither path works perfectly. And that failure — the failure of existing licenses to protect the creators of open-source software from large-scale extraction by cloud providers — is what triggered the license wars.

---

The first shot was fired by MongoDB.

In October 2017, MongoDB went public on the NASDAQ. It was a vindication of the open-source business model — a database company, built on code anyone could download for free, valued at billions by the public markets. Twelve months later, in October 2018, MongoDB changed its license from the AGPL to the Server Side Public License.

The SSPL is a modified version of the AGPL with a single clause expanded to the point of practical impossibility. Section 13 of the AGPL says: if you offer the software as a service, you must release the source code for the service. The SSPL says: if you offer the software as a service, you must release the source code for *everything* — the management software, the user interfaces, the application programming interfaces, the monitoring tools, the backup systems, the hosting software, the automation tools, and everything else required to deploy and run the service.

The requirement is so comprehensive that compliance would mean open-sourcing the entirety of a cloud provider's operational stack. It was designed not to be complied with. It was designed to make cloud hosting of MongoDB by third parties effectively impossible without a commercial license from MongoDB.

The response was immediate and revealing. The Open Source Initiative refused to recognize the SSPL as an open-source license. Red Hat, Debian, and Fedora dropped MongoDB from their package repositories. And Amazon Web Services built Amazon DocumentDB — a MongoDB-compatible but entirely proprietary database. AWS didn't comply with the license. It didn't negotiate a commercial agreement. It built a replacement.

MongoDB survived. More than survived — its revenue continued to grow. The company had proved something important: you could change licenses, alienate the open-source purists, lose your distribution through major Linux distributions, and still build a successful business. The revenue came from enterprises who wanted MongoDB's product, not its license. The license change didn't kill demand. It killed free-riding.

This success emboldened others.

---

In January 2021, Elastic — the company behind Elasticsearch, the search engine that powers logging and analytics for much of the internet — switched from the Apache License 2.0 to a dual license: SSPL plus the Elastic License, a proprietary source-available license. The target, once again, was AWS. Amazon had been offering Elasticsearch as a managed service — Amazon Elasticsearch Service — for years. Elastic's CEO, Shay Banon, was explicit about the reason for the change. [QUOTE NEEDED: Banon's blog post explaining the license switch, specifically his language about AWS]

AWS's response was the most dramatic of the license wars. Rather than build a compatible alternative (as with DocumentDB), AWS forked Elasticsearch itself. Working with Logz.io, CrateDB, Red Hat, and Aiven, Amazon launched OpenSearch — a community-driven fork under the Linux Foundation, licensed under Apache 2.0.

OpenSearch has since developed independently. It has its own roadmap, its own contributors, its own release schedule. In late 2024, Elastic partially reversed course, adding the AGPLv3 as a third licensing option — a partial return to open source that acknowledged the community cost of the SSPL switch. [VERIFY: exact date of Elastic's AGPL addition] But OpenSearch continued regardless. The fork had achieved escape velocity.

---

Redis, the in-memory data store that serves as the caching layer for a significant portion of the internet, had been licensed under the BSD license — about as permissive as licenses get. In March 2024, Redis Labs moved the core Redis project to a dual license: RSAL (Redis Source Available License) plus SSPL.

The reaction was the fastest and most decisive of any license change in the wars. Within weeks, Amazon, Google, Oracle, and Ericsson announced they would back Valkey — a community fork of Redis, starting from version 7.2.4, the last BSD-licensed release. The Linux Foundation provided the institutional home. The fork moved with astonishing speed. By late 2024, surveys indicated that 83 percent of large companies using Redis had either adopted or were actively testing Valkey. [VERIFY: source for the 83% adoption figure]

Then something unusual happened. Salvatore Sanfilippo — known as Antirez, the original creator of Redis — rejoined the project. Antirez had stepped back from day-to-day Redis development in 2020. His return, and his advocacy, helped push Redis toward a reversal. In May 2025, Redis added the AGPLv3 as a licensing option, effectively returning to open source. [VERIFY: exact date of Redis AGPL addition]

But Valkey did not fold. By the time Redis reversed course, Valkey had its own community, its own roadmap, its own release cadence. It had reached version 9 with independent features. [VERIFY: current Valkey version and feature differentiation] The lesson was stark: you can change your license back, but you cannot unfork a fork. The community that left has built its own home, and it has no reason to return.

---

Four license changes in six years. MongoDB, Elastic, HashiCorp, Redis. Each a company that felt the open-source social contract had been violated — that cloud providers were extracting value without reciprocating. Each responded by restricting the terms under which their software could be used. And each triggered a community response: forks, manifestos, migrations.

The pattern repeats with mechanical regularity. Company changes license. Community erupts. Fork announced. Linux Foundation provides institutional home. Cloud providers back the fork. Fork achieves independence. Sometimes the company reverses course. The fork persists anyway.

But look at who backs the forks. Amazon. Google. Oracle. Microsoft. The same cloud providers whose behavior triggered the license changes in the first place. When AWS supports OpenSearch, it is not acting out of principled commitment to open source. It is acting out of commercial interest — it needs permissively licensed databases to offer as managed services. When Google backs Valkey, it is protecting its ability to offer Redis-compatible caching on Google Cloud. The community response is real, and many of the individuals involved are genuinely motivated by open-source principles. But the institutional power behind the forks comes from the companies that caused the problem.

This is what makes the license wars so difficult to adjudicate. The database companies are right: they built the software, and the cloud providers captured the revenue. The cloud providers are right: they are exercising the freedoms the license explicitly granted, and they provide real value through managed services. The community is right: enclosing open-source software violates the norms that made the ecosystem possible. Everyone is right, and the system has no mechanism to resolve the competing claims.

---

There is, however, an intellectual framework that explains why the system broke. It comes not from computer science or copyright law but from political economy — from a woman who spent her career studying fisheries, forests, and irrigation systems.

Elinor Ostrom won the Nobel Prize in Economic Sciences in 2009 — the first woman to receive the award — for her work on common-pool resources. Her contribution was a direct challenge to Garrett Hardin's 1968 thesis, "The Tragedy of the Commons," which argued that shared resources are inevitably overexploited because each individual has an incentive to take as much as possible while bearing only a fraction of the cost. Hardin's conclusion: commons must be either privatized or managed by the state. There is no third option.

Ostrom showed that there was a third option. Studying fishing communities, Swiss alpine pastures, Japanese irrigation systems, and water basins in southern California, she documented hundreds of cases where communities successfully governed shared resources for centuries — without privatization and without state control. The commons did not always end in tragedy. But it didn't govern itself automatically, either. It required institutions.

Ostrom identified eight design principles that characterized successful commons governance. The commons needs clearly defined boundaries — who has the right to extract resources, and who doesn't. It needs rules adapted to local conditions. It needs collective-choice arrangements — the people affected by the rules participate in making them. It needs monitoring. It needs graduated sanctions — not a single catastrophic punishment, but escalating consequences for rule-breakers. It needs conflict-resolution mechanisms. It needs the right to self-organize without external interference. And for large-scale commons, it needs nested governance at multiple levels.

[QUOTE NEEDED: Ostrom on the relationship between boundaries and commons sustainability — from Governing the Commons or a later summary]

Read that list and compare it to the governance of open-source software.

Open source has some of Ostrom's principles. It has collective-choice arrangements — anyone can participate in development, and projects have governance structures (however informal). It has conflict-resolution mechanisms — the ultimate one being the fork, the right of any dissatisfied group to take the code and go their own way. It has the right to self-organize — no external authority tells an open-source project how to run itself.

But open source conspicuously lacks three of Ostrom's principles, and the absence of all three is precisely what the license wars exposed.

First: clearly defined boundaries. Who is "in" the open-source commons? Everyone. That is the point. The MIT License does not distinguish between a solo developer using the code for a side project and a trillion-dollar corporation offering it as a managed service. The license treats all users equally because the philosophy treats all users equally. But Ostrom's work shows that commons without boundaries are commons without the ability to enforce reciprocity. If anyone can extract without limit, the commons depends entirely on goodwill — and goodwill does not scale to trillion-dollar revenue streams.

Second: monitoring. Open-source communities have no systematic way to track who is using their software, how they are using it, or how much value they are extracting. This is by design — monitoring feels like surveillance, and the community is ideologically committed to freedom from surveillance. But without monitoring, there is no way to identify free-riders, no way to measure the gap between extraction and contribution, no way to know when the commons is being depleted.

Third: graduated sanctions. What happens when a cloud provider takes an open-source database and offers it as a service without contributing back? Under a permissive license: nothing. The license allows it. Under the GPL, the SaaS loophole allows it. The only sanction available is social pressure — and social pressure is meaningless to a company with a hundred billion dollars in annual revenue.

The BSL and SSPL revolts were attempts to retroactively install Ostrom's missing principles. They were, in effect, an attempt to add boundaries (you cannot offer this as a commercial service), monitoring (we can tell who is hosting our software), and sanctions (if you violate the terms, you lose your license). The companies that changed their licenses were, whether they knew Ostrom's work or not, trying to build the governance institutions that the open-source commons had been missing from the beginning.

And the fork response — the community's rejection of those boundaries — was the other side of the same coin. The open-source community has built its identity on the absence of boundaries. Boundaries feel like enclosure. Enclosure is the original sin — the thing Stallman rebelled against in 1983, the thing copyleft was designed to prevent. When a company adds restrictions, the community sees enclosure, even when the company sees governance.

The tragedy is not that the commons was exploited. It is that the commons had no way to protect itself without becoming something other than a commons.

---

Beyond software, the commons concept found its most successful legal expression in Creative Commons — the licensing framework created by Lawrence Lessig, Hal Abelson, and Eric Eldred in 2001.

Creative Commons licenses apply not to code but to creative works: text, images, music, educational materials. They offer a menu of permissions and restrictions: CC BY (attribution required), CC BY-SA (attribution plus share-alike — the copyleft equivalent), CC BY-NC (attribution, non-commercial use only), and several combinations. CC0 is the full dedication to the public domain — no restrictions at all.

Wikipedia is licensed under CC BY-SA. Kelty's *Two Bits* — the book that gave us the concept of the recursive public — was published under CC BY-NC-SA. Billions of works worldwide carry Creative Commons licenses. [VERIFY: most recent State of the Commons figure for total CC-licensed works]

Lessig's broader argument — developed in *Free Culture* (2004) and *The Future of Ideas* (2001) — was that copyright had expanded far beyond its original purpose, enclosing culture that should be shared. Creative Commons was the practical answer: a legal toolkit that let creators choose, explicitly and in advance, how much freedom to grant. Not all or nothing, but a spectrum — the same kind of spectrum that software licenses map, applied to human expression.

The parallel to the software license wars is instructive. Creative Commons works because it offers *choice along a spectrum*. A photographer can choose CC BY (use my photo for anything, just credit me) or CC BY-NC-ND (credit me, no commercial use, no modifications). The license fits the creator's values. There is no single "correct" license.

The software world, for decades, treated license choice as a tribal loyalty. You were GPL or you were MIT. Copyleft or permissive. Stallman's camp or Raymond's. The BSL revolt is, among other things, an acknowledgment that the binary was always too simple — that the real needs of software creators exist along a spectrum that neither pure copyleft nor pure permissive licenses fully address.

---

The Business Source License itself is worth understanding, because it represents the clearest attempt to occupy the middle of that spectrum.

The BSL was popularized by Michael "Monty" Widenius — the original creator of MySQL, who also founded MariaDB (the community fork that appeared after Oracle acquired MySQL through its purchase of Sun Microsystems). Widenius had lived both sides of the license wars: he created software that a corporation enclosed, then built a fork to restore it to the commons, then designed a license to prevent the same thing from happening again.

The BSL's mechanism is elegant. The source code is available. You can read it, modify it, use it internally. But you cannot offer it as a hosted commercial service without a commercial agreement from the licensor. And — this is the critical innovation — the restriction is temporary. After a set period, typically four years, the code converts automatically to a fully open-source license, usually Apache 2.0.

The BSL is a time-delayed release valve. It gives the original company a window of commercial protection — enough time to build a business, find customers, establish a brand — and then opens the code to everyone. It is not open source today, but it will be open source in four years, guaranteed.

The Open Source Initiative has been unequivocal: the BSL is not open source. It is "source-available." The distinction matters because the Open Source Definition requires that licenses impose no restrictions on commercial use — and the BSL's prohibition on competitive hosting is explicitly a restriction on commercial use. Whether the BSL is a reasonable compromise or a betrayal of open-source principles depends entirely on whether you think the Open Source Definition is a floor (the minimum acceptable standard of freedom) or a ceiling (the maximum necessary to protect contributors).

---

There is one more dimension to the license wars that deserves attention, because it connects directly to the paradox at the heart of this book.

Every company that changed its license — MongoDB, Elastic, HashiCorp, Redis — built its success on open source. They chose open licenses not out of charity but out of strategy: open source gave them adoption, community, brand recognition, and a user base that no amount of marketing could have purchased. They benefited enormously from the open-source social contract. And then they changed the terms.

Every cloud provider that free-rode on those companies' work — AWS, Azure, Google Cloud — also built its success on open source. The entire cloud computing industry runs on Linux, PostgreSQL, MySQL, Redis, Elasticsearch, and thousands of other open-source projects. The cloud providers benefited enormously from the open-source social contract. And they extracted value at a scale the original creators could not match.

Both sides built their empires on the commons. Both sides changed the game when the commons stopped serving their interests. The companies changed it by restricting licenses. The cloud providers changed it by capturing the monetization layer. Neither side can claim clean hands.

And the community — the developers who wrote the code, filed the bug reports, reviewed the pull requests, and maintained the projects that both sides depend on — the community is the one that gets forked. Literally. They must choose which version to follow, which ecosystem to invest in, which future to bet on. The maintainers who were already underpaid and overworked now face a fragmented landscape where the same software exists under three different names and two different licenses and the politics of which one you use says something about who you are.

---

This is where the chapter's narrative connects forward to what comes next.

The license wars exposed a structural problem in the open-source commons: the absence of governance mechanisms for managing extraction at scale. Ostrom's principles provide the diagnosis. But the open-source community has shown, repeatedly and decisively, that it will not accept the traditional remedies — boundaries, monitoring, sanctions — because those remedies feel like the enclosure the movement was created to resist.

So what works?

A handful of companies figured out an answer. Not by fixing the license problem, but by making it irrelevant. Supabase gives away all of its code — the database, the APIs, the authentication system, the edge functions — under permissive licenses. Anyone can self-host the entire stack. Supabase is valued at approximately five billion dollars. Vercel gives away Next.js under the MIT License. Cloudflare can rebuild it in a week. Vercel is valued at approximately $9.3 billion. GitLab is open core — the community edition is free, the enterprise features are proprietary. HashiCorp, before the BSL switch, followed the same model.

These companies accepted something the BSL companies resisted: the code is not where the value lives. The value lives in the managed service, the developer experience, the deployment pipeline, the support contracts, the brand trust, the operational infrastructure. The code is the loss leader. The platform is the product.

A research consortium studying 44 open-source developer tools between 2020 and 2025 condensed this insight into a single finding that should be tattooed on the forearm of every open-source founder: "Control of distribution and operational infrastructure matters more than control of code." [VERIFY: exact source of the PEXT finding]

That model — open core, closed profit — is the subject of the next chapter. It is the compromise that the open-source economy has, haltingly and imperfectly, converged on. But it is worth naming what the compromise concedes: the code is free, and the freedom of the code is commercially irrelevant. The Four Freedoms apply to a layer of the stack that no longer determines who profits and who doesn't. The real power has migrated upward — from the source code to the infrastructure that runs it.

Stallman freed the code. The cloud freed the profits from the code. And the license wars were the sound of that separation becoming impossible to ignore.

---

*In the next chapter, we follow the money upward — to the companies that built multi-billion-dollar businesses on open foundations, and the surprisingly consistent model they discovered for making openness pay.*
