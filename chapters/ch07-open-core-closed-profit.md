# Chapter 7: Open Core, Closed Profit

In May 2020, a New Zealand developer named Paul Copplestone changed one line on his company's website. He replaced the tagline "Realtime Postgres" with "The Open Source Firebase Alternative." Within three days, the number of hosted databases on his platform went from eight to eight hundred.

The company was Supabase. It had been founded a few weeks earlier. It had no venture capital, a tiny team, and a product that was, by any reasonable standard, unfinished. But the tagline worked because it answered a question that thousands of developers were asking: Where do I go if I don't want to be locked into Google's Firebase? Copplestone's answer was simple. Come here. Everything is open source. If you don't trust us, take the code and leave.

Five years later, Supabase is valued at approximately five billion dollars. It manages over a million active databases. Four million developers use it. Every major component of its technology stack — the database, the API layer, the authentication system, the real-time engine, the file storage — is published under permissive open-source licenses. Anyone can download the entire stack and run it on their own servers, free of charge, forever.

The company makes its money from the people who would rather not.

---

This is the paradox at the center of the most successful open-source companies in the world: they make their fortunes not from the code they write but from the infrastructure that runs it. The code is the gift. The hosting is the business. And the gift is not a trick, not a trial version, not a stripped-down community edition missing the features you actually need. It is the whole thing. Supabase's self-hosted product is functionally identical to its paid cloud service. Vercel's Next.js framework — downloaded two hundred million times per week, powering some of the largest websites on the internet — is MIT-licensed, with no gated features, no enterprise-only modules, no asterisks. [VERIFY: 200M weekly downloads figure]

The previous chapter told the story of companies that tried to solve the open-source business problem with licenses — MongoDB, Elastic, HashiCorp — and the wars that erupted when they changed the terms. This chapter tells the story of companies that solved it by making the license irrelevant. They accepted a proposition that would have seemed suicidal to an earlier generation of software executives: the code has no commercial value. All the value is in the layer above it.

A research consortium studying forty-four open-source developer tools between 2020 and 2025 distilled this insight into a single sentence: "Control of distribution and operational infrastructure matters more than control of code." [VERIFY: exact source of the PEXT finding — authors, publication, date]

That sentence is worth sitting with. It inverts forty years of assumptions about where power lives in the software industry. It says that the thing the open-source movement fought to liberate — source code — is no longer the thing that determines who profits. The battlefield has moved. The code is free. The servers are not.

---

## The Farm Kid and the Firebase Alternative

Paul Copplestone grew up on a farm near Kaikoura, on the northeast coast of New Zealand's South Island. He started coding at eighteen, moved to Singapore, and joined Entrepreneur First — an accelerator that throws founders together and waits to see what sticks. There he met Ant Wilson, a British engineer. They did not start a company together. They lived together for a year. When Copplestone decided he wanted to build an open-source alternative to Firebase, he pitched Wilson the idea over coffee. Wilson said yes.

[QUOTE NEEDED: Copplestone on the founding moment, from Accel podcast or similar]

The pitch was straightforward. Firebase, Google's backend-as-a-service platform, was enormously popular with developers building mobile and web applications. It handled databases, authentication, file storage, and real-time data syncing — the plumbing that every app needs but no one wants to build from scratch. But Firebase was proprietary, tightly coupled to Google Cloud, and increasingly expensive at scale. Developers who built on Firebase discovered, over time, that leaving Firebase meant rebuilding everything.

Copplestone's insight was that every capability Firebase offered could be replicated with existing open-source tools. The database was PostgreSQL — the most trusted relational database in the world, with forty years of development behind it. The API layer was PostgREST, a Haskell service that automatically generates a REST API from a Postgres schema. Authentication was GoTrue, a Go service originally written by Netlify. Real-time subscriptions ran on an Elixir service that listened to Postgres's built-in replication stream. File storage was a Node.js service wrapping standard object storage.

None of these tools were novel. What Supabase built was the glue — the dashboard, the developer experience, the managed infrastructure that made them work together seamlessly. And then it open-sourced the glue, too.

This is the part that confuses people. If everything is open source, what exactly is Supabase selling?

The answer is operations. Supabase Cloud provisions a dedicated Postgres instance for you, configures the API layer, sets up authentication, handles backups, manages scaling, monitors performance, patches security vulnerabilities, and provides a dashboard that makes all of it accessible to a developer who has never touched a database before. You can do all of this yourself with the open-source code. It will take you a week to set up and the rest of your career to maintain. Or you can pay Supabase twenty-five dollars a month and have it running in ninety seconds. [VERIFY: current Pro plan pricing]

The bet is that convenience will always beat self-hosting for the vast majority of users. The numbers suggest the bet is working. Supabase's annual recurring revenue reached approximately seventy million dollars in 2025, up from roughly twenty million a year earlier. [VERIFY: exact revenue timeline] In April 2025, the company raised two hundred million dollars at a two-billion-dollar valuation. Six months later, in October, it raised another hundred million at five billion. The investors included Accel, Peak XV Partners, and Figma Ventures. The stated catalyst for the acceleration was what the tech industry has started calling "vibe coding" — the use of AI tools to generate applications. Every AI-generated app needs a database. Supabase was there to provide one. Two thousand five hundred new databases were being created on the platform every day.

[QUOTE NEEDED: Copplestone or investor on the "vibe coding" growth driver]

What makes Supabase's model distinctive is not just that the code is open source — many companies claim that — but that self-hosting is actively supported. The documentation includes detailed guides for running the entire Supabase stack on your own infrastructure. The Docker Compose configuration is maintained alongside the cloud product. This is the opposite of what most companies do. Most companies with open-source products make self-hosting theoretically possible but practically miserable — missing features, sparse documentation, no support. Supabase treats self-hosting as a trust signal. The implicit message: we are so confident in the value of our managed service that we will help you leave.

---

## The Framework and the Cloud

On the other side of the open-source economy, a similar story was unfolding with different details and the same underlying logic.

Guillermo Rauch is an Argentine software developer who moved to the United States and built a career on developer tools. He created Socket.IO, a widely used real-time communication library. He wrote a book on Node.js. And in 2016, he released Next.js — a React framework that solved a set of problems (server-side rendering, routing, code splitting) that every serious React application eventually encountered.

Next.js is licensed under the MIT License. It is fully open source. It has no premium tier, no gated features, no enterprise edition. Everything the framework can do is available to everyone, for free, without restriction. The framework itself is worth, in commercial terms, nothing.

Rauch's company, Vercel, is valued at $9.3 billion.

The gap between those two numbers — zero and $9.3 billion — is the entire thesis of this chapter.

Rauch has described open source as a "speedrun to product-market fit." [QUOTE NEEDED: verify exact wording and source — likely First Round Review interview] The reasoning is elegant. If developers will not use your software when it is free, when the source code is available, when there are no barriers to adoption whatsoever — then you are building the wrong thing. Open source is the harshest possible filter for product quality. If you survive it, you have something real.

Next.js survived. More than survived — it became the default framework for building React applications. By 2025, it was being downloaded two hundred million times per week. [VERIFY] It powered the web properties of Walmart, TikTok, Nike, and thousands of other companies. It was the foundation of an ecosystem so large that the framework had, for practical purposes, become infrastructure.

And Vercel monetized the infrastructure — not the framework. The company built the best deployment platform for Next.js applications: one-click deployments, global edge network, automatic scaling, serverless functions, image optimization, analytics. The platform worked with any framework, not just Next.js. But the integration with Next.js was, unsurprisingly, the smoothest, the fastest, the most fully realized. Developers who adopted Next.js because it was free and excellent discovered that deploying it on Vercel was free and more excellent.

The business model was usage-based pricing layered on top of a freemium structure. Individual developers could deploy for free. Teams paid twenty dollars per seat per month. Enterprises negotiated custom contracts. And everyone paid for compute, bandwidth, and storage as they scaled. By mid-2025, Vercel's annual recurring revenue had crossed two hundred million dollars — double what it had been fifteen months earlier.

Then Vercel launched v0, an AI-powered code generation tool that could build entire application interfaces from natural language descriptions. Three and a half million users adopted it within months. v0 had its own subscription tier — twenty dollars per month — but its real economic function was to accelerate the creation of applications that would be deployed on Vercel's infrastructure. Every application v0 generated was a potential Vercel customer. The AI product was not separate from the platform business. It was a funnel into it.

[RESEARCH NEEDED: v0 launch date and specific growth metrics]

Rauch understood something that Copplestone also understood, though they expressed it in different languages. The value of open-source software is not in the software itself. The software is a public good — abundant, non-rivalrous, available to everyone. The value is in the *operational context* around the software: the servers that run it, the network that delivers it, the tools that monitor it, the team that maintains it, the experience that makes it easy. That operational context is scarce, rivalrous, and expensive. It is, in economic terms, the perfect thing to sell.

---

## The Finding That Explains Everything

If the Supabase and Vercel stories were isolated cases, they might be dismissed as lucky outliers. They are not. They are instances of a pattern so consistent that it has been formally studied.

Between 2020 and 2025, a research consortium analyzed forty-four open-source developer tool companies — examining their business models, community metrics, funding trajectories, and outcomes. The study, referenced in the literature as the PEXT finding, produced a conclusion that should reshape how anyone thinks about the economics of open source. [VERIFY: full citation for the PEXT study — authors, publication venue, date]

The finding: business model predicts outcomes more reliably than community metrics.

This is a remarkable claim. The open-source world is obsessed with community metrics — GitHub stars, contributor counts, downloads, forks. These numbers are treated as proxies for health, traction, and future success. Investors cite them. Founders brag about them. Conferences celebrate them. And the PEXT research found that they are, at best, weak signals. What matters more — what predicts whether an open-source company will survive, grow, and generate sustainable revenue — is the business model. Specifically: does the company control the distribution and operational infrastructure that sits above the code?

The companies that controlled infrastructure thrived. The companies that controlled only code — no matter how popular, how starred, how forked — struggled. GitHub stars are a measure of developer attention. Operational infrastructure is a measure of developer dependency. Attention is fickle. Dependency is durable.

The equity analyst in me recognizes this pattern immediately. It is the software version of a principle that media companies learned decades ago: content is king, but distribution is emperor. A brilliant movie is worth nothing without theaters or streaming platforms to show it. A brilliant database is worth nothing without servers to run it. The entity that controls the distribution layer captures the majority of the economics, regardless of who created the content.

In the open-source world, this principle has a specific and somewhat uncomfortable implication. It means that the Four Freedoms — Stallman's moral architecture for free software, the right to use, study, modify, and distribute — apply to a layer of the technology stack that is no longer commercially decisive. The code is free. The freedom of the code is real. And the freedom of the code is economically irrelevant.

The money is somewhere else.

---

## The Nonprofit Exception

Not every open-source company plays the venture capital game. Some refuse it on principle. The most successful refusal belongs to a publishing platform called Ghost.

Ghost was founded in 2013 by John O'Nolan, who had been the Deputy Head of the WordPress UI team before striking out on his own. He launched Ghost with a Kickstarter campaign that raised over three hundred thousand dollars — one of the most successful software Kickstarters at the time. [VERIFY: exact Kickstarter amount] But the critical decision came after the campaign: O'Nolan structured Ghost as a non-profit foundation, headquartered in Singapore. No shareholders. No investors. No board demanding quarterly growth. No exit pressure.

Ghost is licensed under the MIT License. The entire codebase is open source. The foundation generates revenue from Ghost(Pro), a managed hosting service — the same model as Supabase and Vercel. But unlike those companies, Ghost has no obligation to maximize returns for venture investors. It has no obligation to grow at all, except to the extent that growth serves its mission: building the best tools for independent publishers and journalists.

By late 2025, Ghost had crossed ten million dollars in annual recurring revenue. [VERIFY: exact date of $10M ARR milestone] The foundation employed thirty-four people. It charged zero transaction fees on the revenue that creators earned through their Ghost publications — a detail that carries moral weight in a landscape where platforms routinely take ten, twenty, or thirty percent of creator earnings. The total revenue that independent publishers had earned through Ghost-powered sites exceeded one hundred and thirty million dollars.

These numbers will never make Ghost a unicorn. O'Nolan will never ring a bell on the NASDAQ. The foundation will never be acquired for six billion dollars. And that is precisely the point.

Ghost demonstrates that the open-core model does not require venture capital. It does not require hypergrowth. It does not require the sword of Damocles that hangs over every VC-funded open-source company: the knowledge that investors expect a return, and that the most reliable way to generate a return is to capture more value, which eventually means restricting the openness that built the community in the first place.

The non-profit structure is Ghost's immune system. It makes the rug pull structurally impossible. There are no shareholders to demand it, no board to approve it, no financial incentive to pursue it. The MIT License will remain the MIT License because there is no one with the authority or the motive to change it.

This raises an uncomfortable question for every VC-funded open-source company: if your code is truly open and your business depends on managed hosting, what happens when the investors want their money back? Supabase has raised over half a billion dollars. Vercel has raised even more. The investors in those rounds did not write those checks out of love for open-source principles. They wrote them because they expect a return — in the form of an IPO, an acquisition, or sustained profitability at scale. If that return does not materialize through the managed-hosting model alone, the pressure to restrict, to gate, to enclose will become intense.

HashiCorp faced exactly that pressure. It started as an open-core company with permissive licenses. When cloud providers captured the hosting revenue, HashiCorp restricted its licenses. The community erupted. The code was forked. And eighteen months later, IBM acquired the company for $6.4 billion. The founders got their return. The open-source community got OpenTofu.

---

## The Landscape

The pattern extends well beyond these case studies.

GitLab, the DevOps platform, is publicly traded on the NASDAQ. It generated $955 million in revenue in its 2026 fiscal year, up twenty-six percent from the prior year. Its model is a textbook open-core arrangement: the Community Edition is free and open source; the Enterprise Edition layers proprietary features — advanced security scanning, compliance tools, priority support — on top. More than half of the Fortune 100 are GitLab customers. The gross margin is eighty-seven percent. But GitLab, unlike Supabase or Vercel, gates features. The community edition is genuinely useful but conspicuously missing the capabilities that large organizations require. The line between "open" and "premium" is the line between what an individual developer needs and what a CISO demands.

Grafana Labs, the observability platform, reached four hundred million dollars in annual recurring revenue by late 2025, with a valuation of six billion dollars. Its core product, Grafana, is open source under the AGPL. The company monetizes through Grafana Cloud — a managed SaaS offering — and Grafana Enterprise Stack for self-hosted deployments with premium features. The numbers reveal something striking: Grafana has twenty million total users and seven thousand paying customers. The company monetizes roughly one percent of its user base. That means ninety-nine percent of the people who use Grafana pay nothing. In any other industry, a ninety-nine percent free-rider rate would be a catastrophe. In open source, it is the business model working as designed. The one percent who pay generate four hundred million dollars a year and margins above eighty percent.

And then there is the cautionary tale. HashiCorp's trajectory — open source, massive adoption, cloud extraction, license restriction, community revolt, corporate acquisition — has become the canonical example of what happens when the open-core model fails to generate enough revenue to satisfy the investors who funded it. IBM's $6.4 billion acquisition in early 2025 was, depending on your perspective, either a vindication (the founders and investors got paid) or a requiem (the open-source community lost the software it had helped build).

Redis offers a postscript. In 2024, Redis Labs switched from a BSD-style license to a dual SSPL/proprietary license — the same move MongoDB had made six years earlier. The community forked the project, creating Valkey under the Linux Foundation's umbrella. Then, in 2025, Redis reversed course. The company added the AGPL as a licensing option, effectively returning to open source. The stated reason: the forks had differentiated themselves enough that Redis felt confident competing on product quality rather than license restriction. [VERIFY: exact timeline of Redis AGPL return and reasoning]

The reversal suggests something important. The rug pull is not always permanent. When the competitive dynamics shift — when forks demonstrate viability, when the community routes around the restriction — some companies discover that openness is, after all, the better strategy. But the damage to trust is real and cumulative. Every license change makes the next developer a little more cautious about building on venture-funded open-source software.

---

## What the Pattern Reveals

Step back from the individual companies and the picture comes into focus.

The open-source economy has stratified into layers, and value has migrated decisively upward. At the bottom sits the source code — the database engines, the frameworks, the libraries, the protocols. This layer is abundant, often excellent, and effectively free. It is governed by the licenses that the previous chapter mapped in detail: MIT, Apache, GPL, AGPL. The Four Freedoms apply here. The code can be used, studied, modified, and distributed. Stallman's dream is realized at this layer.

Above the code sits the operational layer — the hosting, deployment, monitoring, scaling, security, and developer experience that transforms source code into a running service. This layer is scarce, difficult to build well, and expensive to maintain. It is governed not by open-source licenses but by commercial contracts, service-level agreements, and usage-based pricing. The Four Freedoms do not apply here, because there is no source code to free. The operational layer is, by its nature, proprietary — not because of malice or philosophical opposition to openness, but because running infrastructure requires physical resources that someone must pay for.

The companies that understood this stratification early — Supabase, Vercel, Grafana, Ghost — built their businesses on the boundary between the two layers. They contributed generously to the code layer, earning trust and adoption. And they captured revenue at the operational layer, where the economics are favorable and the competition is about execution rather than ideology.

The companies that misunderstood the stratification — or understood it but failed to generate enough operational revenue to satisfy their investors — ended up changing their licenses. MongoDB, Elastic, HashiCorp: each tried to recapture value at the code layer by restricting access to it. Each discovered that the community would not accept the restriction. Each ended up in a different place — MongoDB thrived anyway, Elastic reconciled with open source, HashiCorp was acquired — but all three damaged the trust that their open-source origins had earned.

The PEXT finding is the quantitative confirmation of what these stories illustrate qualitatively. The code does not determine who wins. The infrastructure does. And this insight, once you absorb it, reframes the entire debate about open-source sustainability.

The problem was never that open source is economically unviable. The problem was that the open-source movement — understandably, given its history — located value in the code. Stallman said the code should be free because software is a tool of human freedom. Raymond said the code should be open because openness produces better software. The business school professors said the code should be open because it maximizes network effects and reduces customer acquisition costs. They were all right. And they were all talking about a layer of the stack that, by the 2020s, had been thoroughly commoditized.

The value migrated to infrastructure. The freedom stayed with the code. And the gap between where the freedom lives and where the money lives is the central economic reality of the open-source world today.

---

There is one more dimension to this story, and it leads directly into the next chapter.

The companies profiled here — Supabase, Vercel, GitLab, Grafana, Ghost — are developer tools companies. Their customers are software engineers. Their products are technical infrastructure. Their markets, while large, are bounded by the size of the global developer population.

What happens when a trillion-dollar company applies the same pattern at planetary scale?

Google did not just open-source a framework. It open-sourced a browser engine — Chromium — and a mobile operating system — Android. The logic was identical to what Rauch articulated about Next.js: if you open-source the layer that developers build on, you create an ecosystem that funnels users toward the layer you monetize. For Google, that layer is advertising. Chrome is free. Android is free. The search engine and the app store and the advertising network that sit above them are among the most profitable businesses in the history of capitalism.

The same pattern. The same stratification. The same migration of value from code to infrastructure. But at the scale of billions of users rather than millions of developers, the stakes are different. When Supabase open-sources a database, the consequence is cheaper hosting for startups. When Google open-sources a browser engine, the consequence is market dominance that reshapes the entire web.

The platform play — open-core applied by companies with the resources to make it an instrument of market capture — is the subject of the next chapter. The principles are familiar. The scale changes everything.

---

*The code is free. The servers are not. And the companies that understood this distinction earliest built the most valuable open-source businesses in the world. But what happens when the same logic is applied not by startups seeking product-market fit, but by monopolies seeking market control?*
