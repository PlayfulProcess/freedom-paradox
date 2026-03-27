# Chapter 13: Value Creation for Whom?

There is a question that equity analysts learn before any other. Before discounted cash flow models, before comparable company analysis, before the arcana of revenue recognition and adjusted EBITDA — there is a question so basic that it is almost embarrassing to state.

Who benefits?

Not who says they benefit. Not who the press release claims will benefit. Not who the CEO, in the keynote address with the dramatic lighting and the carefully rehearsed pauses, says the product is designed to serve. Who actually, materially, structurally benefits when this company does this thing?

The question has a Latin name — cui bono — because lawyers have been asking it for two thousand years. It is the first question a prosecutor asks when a body is found. It is the first question a regulator asks when a market moves. And it is the question that has been running beneath every chapter of this book, sometimes explicit, sometimes barely audible, waiting for the moment when the evidence is assembled and the audit can begin.

This is that moment.

---

## The Audit

Twelve chapters of this book have traced the open-source movement from Richard Stallman's anger about a printer through the corporate capture of a freedom ideology and into the AI era, where the stakes of openness have become civilizational. At every turn, someone was making something open. At every turn, someone was benefiting. The two were not always the same party.

Let us be systematic about it.

**Google** open-sourced Chromium, the rendering engine beneath Chrome. The code is genuinely free. Anyone can take it, build a browser, compete with Chrome. Microsoft did exactly that, rebuilding Edge on Chromium's foundation. Brave did it. Opera did it. Samsung did it. The result: more than eighty percent of desktop web traffic now flows through browsers built on Google's open-source code. The web, for practical purposes, runs on Google's engine.

Who benefits? Every browser that adopted Chromium got a world-class rendering engine for free. Developers got a more consistent web platform. Users got faster, more compatible browsers. These are real benefits, genuinely created, widely distributed.

And Google got a world in which eighty percent of web browsing happens inside software that defaults to Google Search, that ships with Google's JavaScript runtime, that implements the standards Google proposes. The advertising revenue that flows through this dominance exceeded three hundred billion dollars in 2024. [VERIFY: exact 2024 Alphabet ad revenue] The open-source browser engine was not a gift. It was the foundation of the most profitable advertising business in human history.

The same logic, applied at planetary scale, produced Android. The operating system is open source under the Apache 2.0 license. Any manufacturer can take the code and build a phone. Hundreds have. The result is 3.9 billion devices, seventy-two percent of the global mobile market, and internet access for billions of people who would otherwise be priced out of the digital world. A farmer in Uttar Pradesh checking crop prices. A student in Lagos accessing educational materials. A seamstress in Jakarta managing her business on WhatsApp. Android made this possible because no proprietary operating system could have achieved this distribution at this price point.

Who benefits? The farmer, the student, the seamstress — genuinely. And Google, which bundles Google Search, Chrome, YouTube, Gmail, and Maps with every device that carries the Play Store. The EU fined Google 4.34 billion euros for the bundling practices. The behavior continued. The open-source layer creates the ecosystem. The proprietary layer captures the revenue. The freedom of the code and the control of the platform are not contradictions. They are complements.

---

**Meta** open-sourced Llama, and Mark Zuckerberg told us exactly why. His open letter accompanying the Llama 3.1 release was startling in its candor: Apple had spent a decade constraining what Meta could build on iOS, taxing Meta's revenue through the App Store, and destroying an estimated ten billion dollars in annual advertising income through App Tracking Transparency. [VERIFY: $10B ATT impact figure] Zuckerberg was not open-sourcing AI because he believed in the commons. He was open-sourcing AI because he had experienced captivity.

The strategy worked — for a while. Llama reached 1.2 billion downloads. Over 140,000 derivative models appeared on Hugging Face. Meta hosted LlamaCon, awarded impact grants, built an API. The ecosystem was real, vast, and growing.

Then it stopped working. Llama 4 underperformed. The benchmarks were, in LeCun's word, "fudged." DeepSeek demonstrated that openness cuts both ways — a Chinese startup used Meta's own research to build a competitive model. And Meta pivoted. Avocado, the company's most ambitious AI project, would be developed behind closed doors by an elite proprietary lab.

Who benefits? Developers who built on Llama got genuine value — capable models, free to deploy, with an active ecosystem. That value persists even as Meta retreats. But Meta's primary beneficiary was always Meta. The open-source strategy was a weapon against Apple's platform control. When the weapon misfired, the company discarded it without ceremony.

The confession was amended, as we noted in Chapter 9. The original version said: we support open source because we learned what it means to be trapped. The amended version says: we support open source when it serves us.

---

**OpenAI** released GPT-OSS under the Apache 2.0 license on a Tuesday. GPT-5 launched on a Thursday. Two days.

The timing was not subtle. The open model was impressive — near-parity with the previous generation's best systems. Developers could download it, fine-tune it, build on it. But the closed model, arriving forty-eight hours later, was better. The open release was a gift that made the paid product look generous by comparison. A customer acquisition cost disguised as an act of idealism.

Who benefits? Developers who adopted GPT-OSS got a genuinely capable model for free. The hospital in Sao Paulo that fine-tunes it for Portuguese-language medical records does not care about OpenAI's strategic timing. The value is real.

And OpenAI got an ecosystem. Every developer who builds on GPT-OSS learns OpenAI's architecture, integrates OpenAI's assumptions, and faces a path of least resistance that leads directly to the paid API when the free model hits its limits. The open model is the first step in a conversion funnel. The frontier model is where the revenue lives.

---

**Alibaba's** Qwen family generated more than 113,000 derivative models by early 2026 — more than Google and Meta combined. Forty-one percent of Hugging Face downloads came from Chinese models. The derivative developers in Berlin and Seoul and Sao Paulo were building on Alibaba's architecture, learning Alibaba's tokenizer, integrating Alibaba's training methodology into their products.

Who benefits? The derivative developers, genuinely. And Alibaba's cloud business, which sits at the top of the upgrade path when those derivatives hit their limits. And, in a dimension that most derivative developers are not thinking about, the strategic interests of a government that views AI ecosystem dominance as a component of national power.

---

**Anthropic** kept Claude closed. It cited safety — the risk of biological misuse, autonomous weapons, authoritarian surveillance. It refused the Pentagon's demand for unrestricted military access. It drew lines at mass surveillance and fully autonomous weapons, and held those lines even as the government moved to designate it a supply chain risk.

Who benefits? If the safety argument is correct — and the evidence for catastrophic misuse risk is not trivial — then the answer is potentially everyone. A world in which frontier AI models cannot be freely downloaded and stripped of safety training is a world in which the barriers to mass harm remain at least partially intact.

But Anthropic also benefits. A closed model is a model that generates revenue through API access. A safety-justified monopoly is still a monopoly. The company that builds the bomb while warning about the blast is also the company that charges for access to the bomb. The RSP v3.0 revision — removing the hard pause commitment under competitive pressure — demonstrated that even the strongest safety commitments erode when the market demands it.

The Electronic Frontier Foundation put it with characteristic precision: the problem is not that Anthropic said no to the Pentagon. The problem is that one person, running one company, was the only thing standing between mass surveillance and the American public.

Who benefits from Anthropic's closure? Humanity, maybe. Anthropic, definitely. Both of these can be true at the same time. The equity analyst's job is to notice that they are.

---

## The PEXT Principle

There is a finding from a research consortium that studied forty-four open-source developer tool companies between 2020 and 2025. It produced a single sentence that, once absorbed, reframes every story in this book. [VERIFY: full PEXT citation]

The finding: control of distribution and operational infrastructure matters more than control of code.

Chapter 7 introduced this principle in the context of Supabase and Vercel — companies that gave away their code and monetized the servers that ran it. But the principle applies universally. It is the skeleton key to the entire open-source economy.

Google controls the distribution of the web (Chrome, Android). Meta controls the distribution of social interaction (Instagram, WhatsApp, Facebook). OpenAI controls the distribution of AI inference (ChatGPT, the API). In every case, the code layer is open or partially open. In every case, the distribution layer is proprietary. In every case, the distribution layer is where the money is.

Stallman's Four Freedoms — the moral architecture that Chapter 3 explored in detail — apply to the code layer. The freedom to use, study, modify, and distribute code is real and meaningful. But that freedom operates in a layer of the technology stack that has been thoroughly commoditized. The code is free. The servers are not. The freedom lives in one place. The money lives in another. And the gap between those two places is the central economic reality of the open-source world.

The PEXT finding, applied to AI, is even more stark. Open weights are the compiled binary — the end product of a process. The true "source" is the training data, the training methodology, the reinforcement learning pipeline, the compute infrastructure. When a company releases model weights but withholds the training data, it is practicing the AI equivalent of releasing a compiled binary without source code. The community gets a model. The lab retains the recipe. The knowledge transfer is deliberately unidirectional.

DeepSeek broke this pattern by publishing its training methodology alongside its weights. That is why DeepSeek was so threatening — not because the model was good, but because the recipe was included. The exception proves the rule. The companies that practice "open behind the frontier" are not sharing knowledge. They are distributing products.

---

## The Spectrum

The equity analyst's instinct might lead to a cynical conclusion: all corporate open source is marketing. But that conclusion would be wrong — not because the strategic motivations are absent, but because the value created for users is real even when the motivations are strategic.

The spectrum runs from cynical to genuine, and the position on it is determined not by rhetoric but by structure.

At one end: **market capture**. Google open-sourced Chromium and Android not as contributions to the commons but as instruments of ecosystem dominance. Meta open-sourced Llama not out of conviction but out of competitive strategy — and abandoned the strategy when it stopped working. These companies create enormous real value through their open-source contributions. They also capture an even more enormous share of the value they create. The gift is genuine. The gift is also a business decision. Both are true.

In the middle: **mutual benefit under tension**. Supabase and Vercel represent something more hopeful. Their code is genuinely open. Self-hosting is actively supported. The interests of the company and the interests of the developer community are, for now, aligned. But "for now" carries a weight that Chapter 7 explored in detail. Both companies have raised hundreds of millions in venture capital. The investors who wrote those checks did not do so out of love for the commons. They expect a return. And the history of VC-funded open-source companies — MongoDB, Elastic, HashiCorp — suggests that the pressure to restrict, to gate, to enclose eventually becomes intense. The alignment of interests is real but structurally fragile.

At the other end: **genuine commons**. Ghost, the publishing platform, is structured as a nonprofit foundation. There are no shareholders. There are no investors demanding returns. There is no mechanism for the rug pull — not because the people involved are more virtuous, but because the structure makes the rug pull impossible. The MIT License will remain the MIT License because no one has the authority or the incentive to change it. Independent publishers have earned more than $130 million through Ghost-powered sites, with zero transaction fees. The value flows to the creators, not to shareholders, because there are no shareholders.

Wikipedia operates on the same principle. The Wikimedia Foundation runs one of the most visited websites in the world on annual donations. No advertising. No paywalls. No data harvesting. No venture capital. The content is Creative Commons licensed. The infrastructure is community-maintained. It is, by any measure, one of the most efficient value-creating institutions in the history of technology.

Creative Commons itself — the legal framework that enables sharing without surrendering all rights — is another example. It is not a company. It is infrastructure for the commons. Governments, universities, artists, and publishers use it to share work on their own terms. No one profits from Creative Commons except the people who use it.

What distinguishes the genuine commons from corporate open source is not the intentions of the people involved. Copplestone at Supabase and O'Nolan at Ghost are both, by all evidence, sincere in their commitment to open source. The difference is structural. Ghost's nonprofit foundation cannot be pressured by investors. Supabase's venture capital can be. The structure determines the long-term behavior, regardless of the founders' values.

---

## The Uncomfortable Truth

Here is what the audit reveals, stated plainly.

Most open source, measured by economic weight, serves corporate interests. The largest open-source projects in the world — Android, Chromium, Kubernetes, TensorFlow, PyTorch, Llama — are maintained by trillion-dollar companies that use them as instruments of ecosystem control. The code is free. The ecosystems built on that code funnel value to the companies that released it. The Four Freedoms apply. The market capture is total.

This does not mean the value created for users is fake. It is not. Android connected billions of people to the internet. Chromium raised browser quality for everyone. Llama derivatives serve hospitals and startups and researchers worldwide. The open-source ecosystem generates genuine, distributed, meaningful value for millions of people who will never buy a Google ad or pay for a Meta API.

But the equity analyst's question remains: who captures the majority of the value? And the answer, overwhelmingly, is the company that controls the layer above the open one. The code is a public good. The distribution is a private moat. The freedom is at the bottom. The money is at the top.

The 1998 rebranding — from "free software" to "open source" — was itself an instance of the pattern. Christine Peterson's insight, which Chapter 4 explored, was that the word "free" scared businesses. The word "open" invited them. The renaming succeeded spectacularly: within a decade, every major technology company had an open-source strategy. But the success came at a cost that Stallman predicted and Raymond dismissed. When you reframe freedom as methodology — when you strip the ethics from the engineering — you make it possible for the most powerful companies in the world to adopt the methodology while ignoring the ethics.

Open source won. And in winning, it became the instrument of the very concentration of power it was designed to prevent.

---

## The Exception That Proves the Rule

Ghost. Wikipedia. Creative Commons. The Apache Software Foundation. The Internet Engineering Task Force. The standards bodies that built the open protocols of the internet itself.

These are not marginal institutions. They are the infrastructure of the digital commons. And they share a structural feature that no venture-funded open-source company can replicate: they are governed by missions, not markets.

Ghost's nonprofit structure makes the rug pull impossible. Wikipedia's donation model makes data harvesting unnecessary. Creative Commons' legal framework makes enclosure unenforceable. These organizations demonstrate that genuine commons can exist, can thrive, and can create value that flows to the public rather than to shareholders.

They also demonstrate something uncomfortable about the limits of the model. Ghost has thirty-four employees and ten million dollars in revenue. Google has 180,000 employees and three hundred billion dollars in advertising revenue. Wikipedia runs on donations. Meta spends $115 billion a year on infrastructure. The genuine commons exist at a scale that is orders of magnitude smaller than the corporate open-source economy. They punch above their weight — Wikipedia's cultural influence far exceeds its budget — but they do not set the terms of the industry.

The question is whether this is a feature or a bug. The optimist says: the genuine commons proves that another model is possible, and its influence is moral rather than economic. The pessimist says: the genuine commons is a rounding error in an economy dominated by corporate interests that have co-opted the language of openness to serve their own ends.

The equity analyst says: both. And then asks the next question.

---

## The Next Question

This chapter has applied a single analytical lens — cui bono — to every open-source narrative in the book. The lens reveals a consistent pattern: corporate open source creates real value for users while capturing disproportionate value for the releasing company. The genuine commons exists as a counterexample but operates at a fraction of the scale. The safety argument for closure is both genuine and self-serving.

None of this is surprising. It is how markets work. Companies optimize for their own interests. The interesting question is not whether they do — of course they do — but whether it matters.

Here is why it matters.

When the thing being opened was a text editor or a database or a web browser, the cui bono question was interesting but not urgent. If Google captured ninety percent of the value from Chromium while creating a better browsing experience for everyone, the arrangement was arguably acceptable. The costs of corporate capture in traditional software are economic — market concentration, reduced competition, higher prices in adjacent markets. These are real costs, but they are manageable.

When the thing being opened is a general-purpose reasoning engine capable of biological weapon design, mass surveillance, autonomous targeting, and the generation of synthetic propaganda at civilizational scale — the cui bono question becomes existential.

Who benefits when Meta releases a model that can be stripped of safety training and deployed by any government on earth? Meta benefits from the ecosystem. Developers benefit from the capability. And any actor with sufficient motivation benefits from the removal of guardrails that only a closed deployment can enforce.

Who benefits when Anthropic keeps its model closed for safety? Humanity benefits, maybe, if the safety argument is correct. Anthropic benefits, definitely, from the competitive moat. And the concentration of power that results — one company, one CEO, one board deciding what the most powerful AI in the world can and cannot do — is precisely the arrangement that the open-source movement spent forty years trying to prevent.

The paradox is now fully visible. Openness in AI can serve freedom — the freedom to build, to study, to innovate, to resist corporate capture. Openness in AI can also serve power — the power to strip safety training, to deploy surveillance, to weaponize a general-purpose reasoning engine. The same act, releasing code freely, serves one or the other depending entirely on context: who does it, why, what they withhold, what structure governs them, and what the technology makes possible.

This is the thesis of the book, crystallized. Openness is not a value. It is a tool. And like every tool, its moral character is determined by the hand that wields it and the purpose it serves.

The remaining question — the question that Part V will take up — is what governance structures can distinguish openness that empowers from openness that endangers. Elinor Ostrom spent a career studying commons that worked. Her principles included boundaries, graduated sanctions, and collective governance by the people affected. The open-source movement resisted all of these. It believed that openness was always better. That freedom was its own governance.

AI is the technology that tests that belief to destruction. The commons that the next chapter enters is not a fishery or a forest. It is a commons that can think. And the question of how to govern it may be the most important question the open-source movement — or any movement — has ever faced.

---

*The equity analyst's first question is who benefits. The philosopher's question, which follows inevitably, is who should. The next chapter takes up both.*
