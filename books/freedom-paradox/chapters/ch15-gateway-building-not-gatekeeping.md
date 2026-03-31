# Chapter 15: Gateway Building, Not Gatekeeping

There is a blog post from 2012 that changed the internet, though almost nobody noticed at the time.

John O'Nolan was twenty-two years old, a web designer who had been contributing to WordPress since he was fourteen. He loved the project — genuinely, in the way that people who build things together love the thing they built. But WordPress had become something other than what it started as. The blogging platform had grown into a content management system, then into an e-commerce engine, then into a platform that could do everything and therefore did nothing simply. O'Nolan wrote a blog post imagining what WordPress would look like if you stripped it back to its essence. Just a blogging platform. Clean, fast, focused on the act of writing.

The post went viral. The demand was so clear, so immediate, that O'Nolan did something unusual. He did not seek venture capital. He did not pitch Sand Hill Road. He launched a Kickstarter campaign with a goal of twenty-five thousand pounds.

It funded in eleven hours. Over twenty-nine days, 5,236 backers pledged a hundred and ninety-six thousand pounds — nearly eight times the goal. Seth Godin backed it. Microsoft backed it. And in September 2013, the first version of Ghost shipped under the MIT license, built by a nonprofit foundation registered in Singapore.

Thirteen years later, Ghost generates over ten million dollars in annual recurring revenue from more than twenty thousand paying customers. It charges zero transaction fees on creator earnings — none. When a writer on Ghost earns a hundred dollars from a subscriber, the writer receives a hundred dollars minus Stripe's processing fee. Compare this with Substack, which takes ten percent. A publication earning sixty thousand dollars a year pays Substack six thousand dollars for the privilege. The same publication on Ghost pays three hundred and forty-eight dollars for hosting.

The difference is structural, not cosmetic. Ghost is a nonprofit. There are no shareholders demanding growth. There is no board optimizing for an IPO. There is no acquirer waiting in the wings. The foundation exists to build publishing tools, and its nonprofit charter makes it, in a legal and fiduciary sense, structurally impossible to betray that mission.

This is not a small thing. This is the thing.

---

## The Architecture of Trust

Every chapter of this book has asked the same question: who benefits? The audit in Chapter 13 revealed a consistent pattern — corporate open source creates genuine value while capturing disproportionate returns. Google's Chromium powers a three-hundred-billion-dollar advertising empire. Meta's Llama built an ecosystem that served Meta's strategic interests until it didn't. OpenAI released GPT-OSS two days before GPT-5, a conversion funnel wearing the costume of a gift.

Chapter 14 introduced Ostrom's principles for governing commons — boundaries, graduated sanctions, collective choice arrangements, monitoring. The open-source movement resisted all of these. It insisted that openness was its own governance. Freedom was the mechanism and the goal simultaneously.

This chapter tells a different story. There are projects that took the open-source ethos seriously and built it into their bones — not just into their license file, but into their corporate structure, their funding model, their governance, their reason for existing. These projects work. They are not as large as their corporate counterparts. They are not as well-funded. But they are durable, and they serve their communities, and the question of who benefits has an answer that does not require footnotes or qualifications.

They are the evidence that the commons can function. And the pattern they share tells us something essential about what it takes.

---

## Ghost: The Structure Is the Protection

In August 2025, Ghost shipped version 6.0 with a feature that no venture-backed newsletter platform would voluntarily build: ActivityPub support. Ghost publications could now federate with Mastodon, Threads, Flipboard, WordPress — any service on the open social web. A writer's audience was no longer locked inside Ghost's walls. It could flow freely across the entire network of federated platforms.

Try to imagine Substack building this. Try to imagine any company whose business model depends on capturing audience attention voluntarily connecting its users to every competing platform on the internet. The exercise is absurd. Substack's value proposition to investors requires that audiences stay on Substack. Ghost's value proposition to writers requires that audiences go wherever writers want them to go.

The difference is not ideological. John O'Nolan is not a more virtuous person than Substack's founders. The difference is structural. Ghost Foundation is a nonprofit. It has no investors. Its incentives are aligned with its users because there is no third party — no shareholder class, no venture fund — whose interests diverge from theirs.

O'Nolan himself wrote a remarkable essay in February 2026, questioning whether open-source licenses mean anything in the age of AI. He described watching Cloudflare take a competitor's open-source codebase and have AI rewrite it from scratch in a week. He wondered aloud whether the entire licensing paradigm — the forty-year infrastructure of GPL and MIT and Apache — was becoming irrelevant.

But here is what O'Nolan's own project demonstrates: Ghost's protection was never primarily the MIT license. The license is necessary — it ensures the code is free, forkable, auditable. But the license alone cannot prevent the kind of corporate capture that this book has documented across twelve chapters. What protects Ghost is the nonprofit structure. The community governance. The funding model that aligns incentives between builder and user. The license is the skeleton. The structure is the body.

---

## Wikipedia: The Miracle and Its Fragility

There is exactly one commons project that operates at true planetary scale. It is not an open-source software company. It is not a crowdfunded startup. It is an encyclopedia maintained by a quarter of a million volunteers, available in more than three hundred languages, funded entirely by donations, carrying no advertising, and licensed under Creative Commons Attribution-ShareAlike.

Wikipedia should not work. Every model of human behavior that economists and organizational theorists have developed says it should not work. Rational actors do not spend thousands of unpaid hours writing and editing encyclopedia articles for strangers. Free-rider problems should destroy contribution incentives. Vandalism should overwhelm quality control. The absence of hierarchical management should produce chaos.

And yet. Six million articles in English alone. Billions of page views per month. A top-ten global website. The single most comprehensive repository of human knowledge ever assembled, built and maintained without a cent of advertising revenue or a single equity investor.

The Wikimedia Foundation's budget for 2025-2026 is two hundred and seven million dollars — substantial, but a rounding error compared to the value Wikipedia creates. The foundation employs engineers who maintain MediaWiki, the GPL-licensed software that runs the encyclopedia. But the content — the actual encyclopedia — is written, edited, fact-checked, and debated by volunteers operating under a governance model that would make a management consultant weep: consensus-based decision-making, community-elected administrators, elaborate dispute resolution processes, and a culture of citation that borders on the obsessive.

The magic is in the license. Creative Commons Attribution-ShareAlike means that anyone can copy, modify, and redistribute Wikipedia's content, but any derivative work must carry the same license. This is copyleft applied to knowledge — the share-alike provision ensures that the commons cannot be enclosed. A corporation cannot take Wikipedia's content, build a proprietary product on it, and lock the improvements away. The knowledge, once freed, stays free.

But the magic is also in the fragility. The Wikimedia Foundation's own data shows continued declines in new and returning editors. The volunteer base that sustains the encyclopedia is aging and not replenishing at historical rates. In the 2024-2025 fiscal year, the foundation dispersed over eighteen million dollars in grants to support volunteers and affiliates — an acknowledgment that the commons does not sustain itself through good intentions alone.

Wikipedia is the strongest evidence that commons-based peer production works. It is also a reminder that the commons is a garden, not a wilderness. It requires tending. The moment the gardeners stop showing up, the weeds move in.

---

## Creative Commons: The Infrastructure of Sharing

In 2001, Lawrence Lessig — a Stanford law professor who had spent the previous decade watching copyright law expand into a mechanism for controlling digital culture — founded an organization with a deceptively modest mission: give creators a simple way to share their work.

The insight was elegant. Copyright law's default setting is total restriction: all rights reserved. Every photograph, every blog post, every sketch on a napkin is automatically copyrighted the moment it is created. If you want to share your work — if you want to give explicit permission for others to use, remix, and build upon it — you need a license. But drafting a license requires a lawyer, which costs money, which means that the legal tools for sharing are available primarily to those who can afford them.

Creative Commons created a suite of standardized licenses — human-readable, machine-readable, legally enforceable — that anyone could attach to their work with a few clicks. CC BY lets others use your work with attribution. CC BY-SA adds the copyleft requirement: derivatives must carry the same license. CC BY-NC restricts commercial use. CC0 dedicates the work to the public domain entirely.

Twenty-five years later, more than two billion works carry Creative Commons licenses. Flickr hosts over four hundred million CC-licensed photographs. Wikimedia Commons holds tens of millions. YouTube, DeviantArt, academic journals, government databases, textbook initiatives — the infrastructure of sharing that Lessig built has become so ubiquitous that most people who benefit from it do not know it exists.

This is what successful commons infrastructure looks like: invisible. You do not notice the bridge when you are driving across it. You notice its absence when it collapses.

And it may be collapsing. The AI training data question has put Creative Commons licenses under unprecedented strain. When Lessig designed CC licenses in 2001, the use case was human sharing — a photographer letting a blogger use her image, a musician letting a filmmaker use his track. Nobody anticipated that the primary consumer of CC-licensed works would be machine learning systems ingesting billions of images and texts to train models that compete with the original creators.

Creative Commons has acknowledged this challenge directly. Its 2025 and 2026 strategic focus includes ensuring that technological change strengthens the commons rather than undermining it. But the organization is navigating a paradox that its founder could not have imagined: the legal tools designed to make sharing easier may be making extraction easier too.

---

## The Chosen: Equity Crowdfunding and the Faith Commons

In 2017, a filmmaker named Dallas Jenkins wanted to make a television series about the life of Jesus. No network would fund it. The subject was too niche, the audience too uncertain, the risk too high for a system that measures value in advertising demographics.

Jenkins and his team turned to a provision of the JOBS Act that had gone into effect in 2016, allowing companies to offer equity to non-accredited investors through regulated crowdfunding platforms. This was not Kickstarter-style reward crowdfunding, where backers receive a T-shirt and a thank-you email. This was equity crowdfunding. Sixteen thousand people invested real money and received real shares of ownership in the production.

They raised eleven million dollars — the largest crowdfunding campaign for a television series in history, surpassing the previous record holder by nearly double.

The terms were structured to protect investors: the production's managers guaranteed they would take no profits until every investor received at least a hundred and twenty percent return on their investment. The show would be distributed for free through an app, with a pay-it-forward model — viewers who could afford to contribute would pay to unlock episodes for those who could not.

By 2025, The Chosen had reached more than three hundred million viewers in a hundred and seventy-five countries. It had been translated into more than fifty languages. Nearly a billion episode views. Subsequent seasons were funded by continued crowdfunding — over thirty-seven million dollars total, with nearly twenty-eight million raised for the seventh and final season alone.

The model is genuinely innovative. It proved that audiences, not networks, could finance major media production. It proved that free distribution subsidized by a passionate minority could achieve scale that traditional distribution models could not. And it demonstrated that the JOBS Act's equity crowdfunding provisions — designed primarily for startups — could be applied to cultural production.

But the model also reveals the limits of commons-based cultural funding. Fewer than five percent of The Chosen's viewers contribute financially — a figure that Dallas Jenkins has repeatedly cited in interviews and fundraising appeals. The production depends on the extraordinary generosity of a small fraction of its audience. And as the series scaled, it gravitated toward traditional distribution: in 2025, Jenkins announced a deal with Amazon MGM Studios for theatrical premieres and a ninety-day exclusivity window on Prime Video before episodes become free.

The trajectory is instructive. Even the most successful commons-adjacent media project, built on equity crowdfunding and free distribution, eventually found that the economics of scale push toward partnership with exactly the kind of institutional distributor the project was designed to circumvent.

---

## Open Hardware: When Atoms Want to Be Free

The open-source philosophy was born in software, where the marginal cost of copying is zero. Sharing code costs nothing. But a movement has been testing whether the same principles apply to physical things — hardware, circuits, processor architectures — where sharing means sharing designs that must still be manufactured in silicon and steel.

RISC-V is the most consequential experiment. An open instruction set architecture — the fundamental specification that tells a processor how to execute software — developed at UC Berkeley and released under a BSD license. Any company can design, manufacture, and sell RISC-V processors without paying licensing fees. Compare this with ARM, the dominant architecture for mobile devices, which charges licensing fees that can reach tens of millions of dollars for high-performance designs.

One billion RISC-V cores shipped in 2024 alone. By late 2025, the architecture had achieved twenty-five percent market penetration — a figure that would have been inconceivable five years earlier. Qualcomm acquired Ventana Micro Systems for two point four billion dollars. Meta acquired Rivos. Both moves signaled that the industry's two largest consumers of ARM processors were building RISC-V roadmaps.

Arduino democratized physical computing with open-source hardware designs under Creative Commons licenses, making it possible for students and hobbyists to build electronic prototypes without proprietary tools. The Open Compute Project, founded by Facebook in 2011, open-sourced data center hardware designs that saved the company over a billion dollars — and, because the designs were shared, saved every member of the four-hundred-company consortium as well.

The equity analyst in me notes the familiar pattern: Facebook founded OCP because open hardware served Facebook's interests. The same cui bono logic from Chapter 13 applies. But there is a difference. OCP's open designs genuinely reduced costs across the industry. The savings were not captured solely by Facebook. The commons, in this case, created value that was broadly distributed — not because Facebook was altruistic, but because the structure of open hardware standards makes exclusive capture difficult.

When a design is open, any manufacturer can build it. The competition is in manufacturing, not in licensing. The value shifts from intellectual property rent to operational efficiency. This is not a utopian outcome — it is a market outcome that happens to align with the commons because the commons, in this case, serves every participant's interests simultaneously.

---

## Platform Cooperativism: The Oldest Structure

Before open source, before Creative Commons, before crowdfunding, there were cooperatives. Worker-owned businesses governed by the principle of one member, one vote, with profits distributed to the people who created them.

The platform economy gave this old idea a new application. Stocksy United, a stock photography platform based in Victoria, British Columbia, is collectively owned by nearly a thousand photographers. It was founded by the former owners of iStockphoto, who had sold their creation to Getty Images and watched it deteriorate. They built Stocksy as the antidote: photographer-owned, with ninety percent of profits distributed to artists. No venture capital. No exit strategy. No incentive to degrade quality in pursuit of volume.

Up & Go is a cleaning cooperative in New York City that operates as a platform — workers accept jobs, set their own pay rates, and share ownership of the enterprise. CoopCycle is a cooperative food delivery network that operates across European cities. The Drivers Cooperative in New York City offers ride-hail services owned by the drivers themselves.

These are small projects. Stocksy's revenue is a fraction of Getty's. Up & Go cleans apartments; it does not threaten Uber. The Drivers Cooperative serves a borough, not a continent. Platform cooperativism is, at present, a proof of concept more than a market force.

But the proof matters. These cooperatives demonstrate that the platform model — two-sided marketplaces connecting providers with customers through software — does not require venture capital or extractive fee structures. The technology is neutral. The ownership structure determines who benefits.

---

## The Pattern

What do Ghost, Wikipedia, Creative Commons, The Chosen, RISC-V, Arduino, Stocksy, and Up & Go have in common?

None of them are merely open. Each of them is structurally protected.

Ghost is not just MIT-licensed. It is a nonprofit foundation whose charter prevents sale or extractive pivot. Wikipedia is not just CC BY-SA. It is governed by a community with elected administrators, consensus processes, and a nonprofit foundation that has resisted advertising for a quarter century. Creative Commons did not just create licenses. It created legal infrastructure that standardized sharing at planetary scale. The Chosen did not just ask for donations. It offered equity — real ownership — to its audience. RISC-V is not just an open specification. It is governed by RISC-V International, a nonprofit organization in Switzerland. Stocksy is not just a photography platform. It is a cooperative where the photographers own the company.

The common thread is not openness. The common thread is governance.

Each of these projects answered a question that the open-source movement, in its idealistic first decades, preferred not to ask: what prevents the commons from being captured? Richard Stallman's answer was copyleft — the GPL's viral licensing requirement that derivatives must remain free. It was a brilliant structural innovation. But copyleft alone, as the previous twelve chapters have demonstrated, does not prevent corporate capture. Companies learned to work around copyleft, to build proprietary services on top of copyleft foundations, to use permissive licenses that impose no requirements at all.

The projects in this chapter went further. They did not rely on the license alone. They built the protection into the institution — into the corporate charter, the ownership structure, the governance model, the funding mechanism. The license says the code is free. The structure says the project is free. These are different claims, and only the second one has proven durable.

---

## The Scale Question

There is an objection that must be addressed directly: these projects are small.

Ghost has twenty thousand customers. Substack has millions of readers. Wikipedia is the exception, but Wikipedia operates in a domain — encyclopedic knowledge — with unique properties: it is non-rival, non-excludable, and improves with every contribution. Not every commons has these properties. Stocksy has a thousand photographers. Getty has hundreds of thousands. The Drivers Cooperative operates in one city. Uber operates in seventy countries.

The scale gap is real, and it has a structural explanation. Venture capital accelerates growth by subsidizing losses. A VC-backed company can offer its product below cost for years, burning through investor capital to acquire users, build network effects, and establish the kind of dominance that eventually generates returns. A nonprofit or cooperative cannot do this. It must be sustainable from the beginning, which means it grows at the speed its community can support — not at the speed investors demand.

This is not a failure of the commons model. It is a feature. The venture-capital growth model produces the scale advantages documented in Part III of this book — and also the extractive outcomes. The commons model produces smaller, more durable, more equitable outcomes — and also the limits. Ghost will probably never have Substack's readership. But Ghost will also never take ten percent of its writers' earnings to fund a pivot that serves investors rather than creators.

The question is not whether commons projects can beat corporate projects at the corporate game. They cannot, and they should not try. The question is whether commons projects can build durable alternatives that serve their communities well — and whether, in the domains where the stakes are highest, the commons model offers something that the corporate model structurally cannot.

---

## Gateway Building

The title of this chapter contains a distinction that matters.

Gatekeeping is the use of control to extract value. The gatekeeper stands between the creator and the audience, between the developer and the user, between the citizen and the resource — and charges a toll. Substack's ten percent fee is a toll. ARM's licensing fees are a toll. Getty's terms are a toll. The toll is not inherently wrong — gatekeepers often provide genuine services — but the incentive is always to raise the toll, to increase the dependency, to make the gate harder to bypass.

Gateway building is the use of openness to create access. The gateway builder constructs the infrastructure through which value flows — and then steps aside. Creative Commons built the legal gateway through which two billion works entered the commons. Wikipedia built the knowledge gateway through which billions of readers access human knowledge. Ghost built the publishing gateway through which twenty thousand creators reach their audiences without paying a toll. RISC-V built the processor gateway through which a billion chips entered the market without licensing fees.

The distinction is not about profit. Ghost generates ten million dollars a year. Wikimedia Foundation operates on a two-hundred-million-dollar budget. RISC-V International charges membership fees. Gateway builders can sustain themselves financially. The distinction is about structural alignment: whose interests does the institution serve, by design, when the interests of different stakeholders diverge?

A venture-backed company serves its investors first, its users second. This is not cynicism; it is fiduciary duty. A nonprofit serves its mission. A cooperative serves its members. The structural alignment is built into the legal charter, not into the press release.

---

## What This Means for AI

The projects in this chapter share one more property, the one that connects them to the argument of this book: the things they open are generative.

Publishing tools. Encyclopedic knowledge. Creative works. Hardware designs. Cleaning services. Stock photography. Television. These are things that create more value when shared. A published essay is more valuable when more people read it. A hardware design is more useful when more manufacturers can build it. A photograph is more powerful when more creators can incorporate it into their work.

AI is different.

A language model that can generate convincing propaganda is more dangerous when more actors can deploy it. A biological design tool is more dangerous when more people can strip its safety training. A surveillance system is more dangerous when more governments can customize it without oversight.

The projects in this chapter work because the thing being opened is generative — and because the structural protections prevent capture without preventing use. Ghost's nonprofit structure prevents Substack-style extraction without preventing anyone from forking the code and building their own publishing platform. Wikipedia's CC BY-SA license prevents proprietary enclosure without preventing anyone from reading, copying, or building upon the encyclopedia. The boundaries are permeable in the direction of creation and impermeable in the direction of extraction.

AI governance requires something analogous but more complex: boundaries that are permeable in the direction of beneficial use and impermeable in the direction of catastrophic misuse. The structural protections that work for publishing tools and encyclopedias — nonprofit status, copyleft licenses, community governance — are necessary but insufficient for a technology that can be weaponized.

The commons that can think, as Chapter 14 established, requires governance that the commons that can publish does not. But the projects in this chapter prove that governance is possible. They prove that structural protection and openness are not contradictions. They prove that the choice is not between total openness and total closure.

There is a space between. It is the space that Ghost occupies, and Wikipedia, and Creative Commons, and every cooperative and commons project that built its protections into its structure rather than relying on the goodwill of its founders.

The final chapter will ask what that space looks like for AI — the technology that tests every principle this book has examined. But first, this: the commons works. It works at the scale of a newsletter platform and the scale of an encyclopedia. It works for publishing and for hardware and for photography and for television. It works when the protections are real, when the governance is genuine, when the structure aligns incentives between builder and user.

The question is not whether we can build commons that work. We already have. The question is whether we can build commons that work for the most powerful technology humans have ever created — commons that preserve the freedom to innovate while governing the capacity to destroy.

That question, and this book's answer to it, belongs to the final chapter.

---

*The commons that works is the commons that was designed to work. Freedom is not the absence of structure. Freedom is the presence of the right structure. The next chapter names the paradox.*
