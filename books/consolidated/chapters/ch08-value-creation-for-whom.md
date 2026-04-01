# Chapter 8: Value Creation for Whom?

There is a question that equity analysts learn before any other. Before discounted cash flow models, before comparable company analysis, before the arcana of revenue recognition and adjusted EBITDA — there is a question so basic that it is almost embarrassing to state.

Who benefits?

Not who says they benefit. Not who the press release claims will benefit. Not who the CEO, in the keynote address with the dramatic lighting and the carefully rehearsed pauses, says the product is designed to serve. Who actually, materially, structurally benefits when this company does this thing?

The question has a Latin name — cui bono — because lawyers have been asking it for two thousand years. It is the first question a prosecutor asks when a body is found. It is the first question a regulator asks when a market moves. And it is the question that has been running beneath every chapter of this book, sometimes explicit, sometimes barely audible, waiting for the moment when the evidence is assembled and the audit can begin.

This is that moment.

---

## The Confession

In July 2024, Mark Zuckerberg did something unusual for a tech CEO: he told the truth about why he was doing what he was doing.

The occasion was the release of Llama 3.1, Meta's latest large language model, which the company was making available for anyone to download, modify, and deploy. Alongside the release, Zuckerberg published an open letter titled "Open Source AI Is the Path Forward." Most corporate manifestos bury their real motivations under layers of altruistic language. Zuckerberg's letter contained a confession so direct it was almost startling.

"One of my formative experiences," he wrote, "has been building our services constrained by what Apple will let us build on their platforms. Between the way they tax developers, the arbitrary rules they apply, and all the product innovations they block from shipping..."

There it was. Not a lofty argument about the commons or the future of knowledge. A wound. Apple had spent a decade dictating what Meta could build, how it could monetize, and what data it could access. The App Tracking Transparency framework alone had cost Meta an estimated ten billion dollars in annual advertising revenue. Zuckerberg wasn't open-sourcing AI because he believed in freedom. He was open-sourcing AI because he had experienced captivity.

The strategy worked — for a while. Meta sells advertising, not AI. Its models power recommendation algorithms, content moderation, ad targeting, and the chatbot features across Instagram, WhatsApp, and Facebook. Releasing the models strengthened Meta's position: every developer who built on Llama created another node in an ecosystem that defaulted to Meta's infrastructure. Llama was the new Android: give away the technology to own the ecosystem.

By the time Meta hosted LlamaCon — its first-ever developer conference dedicated to Llama, modeled on Apple's WWDC — downloads had reached 1.2 billion, with an average of one million per day.

Then the earthquake hit. DeepSeek, a Chinese startup operating under US chip sanctions, used Meta's openly shared research to build a model that rivaled Meta's own. The open-source philosophy was vindicated — and the competitive risk was made vivid in a single event.

What followed was swift. Llama 4 underperformed. Independent researchers discovered that Meta's benchmark submissions used an unreleased "experimental" variant; the publicly available model landed in thirty-second place. The benchmarks had been, in Yann LeCun's own word, "fudged." Zuckerberg sidelined the GenAI team, hired Scale AI's founder as Chief AI Officer, and began developing Avocado — a model that, according to multiple reports, might not be open source at all.

The confession was amended. The original version said: we support open source because we learned what it means to be trapped. The amended version says: we support open source when it serves us.

---

## The Audit

Apply the equity analyst's question systematically across every open-source narrative in this book.

**Google** open-sourced Chromium and Android. The code is genuinely free. Anyone can take it, build a browser, compete with Chrome. Microsoft did exactly that. The result: more than eighty percent of desktop web traffic flows through browsers built on Google's open-source code. Android runs on 3.9 billion devices. A farmer in Uttar Pradesh checking crop prices, a student in Lagos accessing educational materials, a seamstress in Jakarta managing her business on WhatsApp — Android made this possible because no proprietary operating system could have achieved this distribution at this price point.

Who benefits? The farmer, the student, the seamstress — genuinely. And Google, which bundles Search, Chrome, YouTube, Gmail, and Maps with every device that carries the Play Store. The advertising revenue flowing through this dominance reached $264.6 billion in 2024. The open-source layer creates the ecosystem. The proprietary layer captures the revenue.

**OpenAI** released GPT-OSS under the Apache 2.0 license on a Tuesday. GPT-5 launched on a Thursday. Two days. The open model was impressive — near-parity with the previous generation. The closed model, arriving forty-eight hours later, was better. Every developer who builds on GPT-OSS learns OpenAI's architecture and faces a path of least resistance leading directly to the paid API.

**Alibaba's** Qwen family generated more than 113,000 derivative models — more than Google and Meta combined. Forty-one percent of Hugging Face downloads came from Chinese models. The derivative developers in Berlin and Seoul and São Paulo were building on Alibaba's architecture. And at the top of the upgrade path sat Alibaba's cloud business — and the strategic interests of a government that views AI ecosystem dominance as a component of national power.

**Anthropic** kept Claude closed. It cited safety — biological misuse, autonomous weapons, authoritarian surveillance. It refused the Pentagon's demand for unrestricted military access. Who benefits? If the safety argument is correct, potentially everyone. But Anthropic also benefits. A safety-justified monopoly is still a monopoly. As the Electronic Frontier Foundation put it: the problem is not that Anthropic said no to the Pentagon. The problem is that one person, running one company, was the only thing standing between mass surveillance and the American public.

---

## The PEXT Principle

A research consortium called PEXT studied forty-four open-source developer tool companies between 2020 and 2025. Their finding, once absorbed, reframes every story in this book: control of distribution and operational infrastructure matters more than control of code.

Google controls the distribution of the web. Meta controls the distribution of social interaction. OpenAI controls the distribution of AI inference. In every case, the code layer is open or partially open. In every case, the distribution layer is proprietary. In every case, the distribution layer is where the money is.

Stallman's Four Freedoms apply to the code layer. But that freedom operates in a layer that has been thoroughly commoditized. The code is free. The servers are not. The freedom lives in one place. The money lives in another. And the gap between those two places is the central economic reality of the open-source world.

The 1998 rebranding — from "free software" to "open source" — was itself an instance of the pattern. When you reframe freedom as methodology, when you strip the ethics from the engineering, you make it possible for the most powerful companies in the world to adopt the methodology while ignoring the ethics.

Open source won. And in winning, it became the instrument of the very concentration of power it was designed to prevent.

---

## The Exception

Ghost. Wikipedia. Creative Commons. The Apache Software Foundation. The Internet Engineering Task Force.

These are not marginal institutions. They are the infrastructure of the digital commons. And they share a structural feature no venture-funded company can replicate: they are governed by missions, not markets.

Ghost's nonprofit structure makes the rug pull impossible. Wikipedia's donation model makes data harvesting unnecessary. Creative Commons' legal framework makes enclosure unenforceable. Independent publishers have earned more than $130 million through Ghost-powered sites, with zero transaction fees.

They also demonstrate the limits of the model. Ghost has thirty-four employees and ten million dollars in revenue. Google has 180,000 employees and three hundred billion in advertising revenue. The genuine commons exists at a scale orders of magnitude smaller than the corporate open-source economy. It punches above its weight — Wikipedia's cultural influence far exceeds its budget — but it does not set the terms of the industry.

---

## The Uncomfortable Truth

Most open source, measured by economic weight, serves corporate interests. The largest projects — Android, Chromium, Kubernetes, PyTorch, Llama — are maintained by trillion-dollar companies that use them as instruments of ecosystem control. The code is free. The ecosystems built on that code funnel value to the companies that released it.

This does not mean the value created for users is fake. It is not. Android connected billions. Chromium raised browser quality. Llama derivatives serve hospitals and researchers worldwide. The open-source ecosystem generates genuine value for millions of people who will never buy a Google ad or pay for a Meta API.

But the equity analyst's question remains: who captures the majority of the value? The company that controls the layer above the open one. The code is a public good. The distribution is a private moat. The freedom is at the bottom. The money is at the top.

Openness is not a value. It is a tool. And like every tool, its moral character is determined by the hand that wields it and the purpose it serves.
