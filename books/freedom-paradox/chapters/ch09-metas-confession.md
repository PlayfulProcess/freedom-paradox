# Chapter 9: Meta's Confession

In July 2024, Mark Zuckerberg did something unusual for a tech CEO: he told the truth about why he was doing what he was doing.

The occasion was the release of Llama 3.1, Meta's latest large language model, which the company was making available for anyone to download, modify, and deploy. Alongside the release, Zuckerberg published an open letter titled "Open Source AI Is the Path Forward." Most corporate manifestos bury their real motivations under layers of altruistic language — democratizing technology, empowering developers, advancing humanity. Zuckerberg's letter did some of that, too. But it also contained a confession so direct it was almost startling.

"One of my formative experiences," he wrote, "has been building our services constrained by what Apple will let us build on their platforms. Between the way they tax developers, the arbitrary rules they apply, and all the product innovations they block from shipping..."

There it was. Not a lofty argument about the commons or the future of knowledge. A wound. Apple had spent a decade dictating what Meta could build, how it could monetize, and what data it could access. The App Tracking Transparency framework alone had cost Meta an estimated ten billion dollars in annual advertising revenue. The message was unmistakable: Zuckerberg wasn't open-sourcing AI because he believed in freedom. He was open-sourcing AI because he had experienced captivity.

The letter went further. "It's clear that Meta and many other companies would be freed up to build much better services for people if we could build the best versions of our products and competitors were not able to constrain what we could build." He extended the argument to AR and VR, to the next generation of computing platforms. Open source wasn't just good policy. It was insurance against ever being trapped again.

This was the open-core logic from the previous chapters, stripped of pretense. Google had open-sourced Android to prevent Microsoft from controlling the mobile platform layer. Red Hat had built a billion-dollar business by wrapping free software in enterprise services. Now Meta was applying the same pattern to the most powerful technology of the current era — and its CEO was willing to say exactly why.

---

## The Strategic Calculus

The honesty of Zuckerberg's letter was possible because of a structural reality that made Meta's position genuinely different from its competitors. OpenAI sells subscriptions and API access. Google sells cloud computing. Anthropic sells safety-wrapped AI services. For these companies, releasing their best models for free would be commercial suicide.

Meta sells advertising.

Its AI models power recommendation algorithms, content moderation, ad targeting, and the chatbot features embedded across Instagram, WhatsApp, and Facebook. None of these revenue streams require keeping the underlying models proprietary. If anything, releasing the models strengthens Meta's position: every developer who builds on Llama creates another node in an ecosystem that defaults to Meta's infrastructure, tools, and eventually its API services.

This is the same economic logic that made Android free. Google didn't need to charge for a mobile operating system because it made money from search, advertising, and data collection. The operating system was a means to an end — a way to ensure that the next billion internet users accessed the web through Google's services rather than a competitor's. Meta's AI strategy followed the identical playbook. Llama was the new Android: give away the technology to own the ecosystem.

The numbers suggested the strategy was working spectacularly. By December 2024, Llama models had been downloaded 650 million times. Three months later, in March 2025, Zuckerberg announced they had crossed one billion. By the time Meta hosted LlamaCon — its first-ever developer conference dedicated to the Llama family, modeled consciously on Apple's WWDC — the count had reached 1.2 billion downloads, with an average of one million per day. Enterprise customers included Spotify, AT&T, and DoorDash. The ecosystem was real, it was vast, and it was growing.

LlamaCon itself was a statement of ambition. Meta announced the Llama API — customizable, compatible with OpenAI's SDK, explicitly no lock-in. It released Llama Guard 4 and LlamaFirewall, security tools for the open-source community. It awarded $1.5 million in Llama Impact Grants. It announced partnerships with Cerebras and Groq for faster inference. This was not the behavior of a company grudgingly releasing research artifacts. This was a company building a platform.

<!-- PP: The LlamaCon section could use more flavor. Was there video of Zuckerberg presenting? What was the vibe? Developer conferences have a liturgical quality worth capturing. -->

---

## The Name Game

But what, exactly, had Meta released?

The Open Source Initiative had been asking this question since Llama 2 arrived in July 2023, and by 2025 the answer had become a flashpoint. In October 2024, the OSI published its formal Open Source AI Definition, establishing clear criteria for when an AI system qualifies as genuinely open source. The model's weights and training code must be openly available. The training data must be described in sufficient detail for the model to be substantially reproduced. And the license must allow use for any purpose, by any person, without restriction.

Llama failed on every count.

The license prohibited commercial use by applications with more than 700 million monthly active users — a restriction aimed squarely at Meta's competitors. It included an acceptable use policy that barred deployment in areas like regulated substances and critical infrastructure. It imposed geographic restrictions that, as the OSI noted when Llama 4 launched, excluded Europeans from certain uses. And most critically, Meta disclosed nothing about its training data: not what was in it, not how it was collected, not how it was cleaned. The model was a black box that happened to have its parameters visible.

"Meta is trying to redefine Open Source for their own benefit," the OSI wrote in February 2025, "and at the expense of our freedom."

The Free Software Foundation weighed in the following month, classifying the Llama 3.1 license as nonfree software. This was the institutional apparatus of the free software movement — the organizations that Richard Stallman and his successors had built over four decades — rendering a formal judgment: whatever Meta was doing, it was not open source.

What Meta was doing, the emerging terminology suggested, was releasing "open weights." The distinction matters. An open-weights model shares its learned parameters — the billions of numbers that encode the model's knowledge — but withholds the training data, the training code, and the full methodology. You can run the model. You can fine-tune it. You can build applications on top of it. But you cannot reproduce it, audit it for bias, verify its safety claims, or understand why it behaves the way it does. As one analysis put it: open weights enable replication; open source enables advancement.

This was not a new pattern. It was the license wars of Chapter 6 transposed into a new technological context, with a new question at its center: what counts as "source" when the artifact is not code but a neural network? For traditional software, the source code is the human-readable form from which the executable is compiled. For an AI model, the weights are more like the compiled binary — the end product of a process. The true "source" is the combination of training data, training code, hyperparameters, and computational infrastructure that produced those weights. By this logic, releasing weights without training data is the AI equivalent of releasing a compiled binary without source code. It is precisely the kind of strategic half-openness that the free software movement was created to resist.

<!-- PP: This is one of the most important sections of the chapter. The "open weights = compiled binary" analogy might be the single most clarifying thing in the whole book. Make sure this comes through clearly. -->

---

## The Earthquake

On January 20, 2025, a Chinese AI startup called DeepSeek released a model that changed everything.

DeepSeek-R1 was a reasoning model that demonstrated capabilities comparable to the best Western frontier models — at a reported fraction of the training cost. Within days, it had overtaken ChatGPT as the most-downloaded free app on the Apple App Store in the United States. The AI industry, which had organized itself around the assumption that building frontier models required billions of dollars and tens of thousands of Nvidia GPUs, was suddenly confronted with evidence that the assumption might be wrong.

For Meta, DeepSeek was both vindication and threat, and the company's response revealed the tension between the two.

Yann LeCun, Meta's chief AI scientist and the intellectual architect of its open-source strategy, seized on the vindication narrative. DeepSeek, he argued, proved that open models were surpassing proprietary ones. The startup had built on publicly available research, including PyTorch (created at Meta) and architectural insights from Llama itself. They had improved upon it and released their work openly. This was exactly how open source was supposed to function: a virtuous cycle of building, sharing, and improving.

LeCun was not wrong. DeepSeek's success was a genuine demonstration of the power of open research. It forced OpenAI to release its first open model in six years. It emboldened a wave of open-source development globally. Meta's stock actually rose on the news — Wall Street, at least initially, interpreted DeepSeek as evidence that Meta's bet on open AI was paying off.

But the vindication story had a shadow. DeepSeek had not merely validated the philosophy of openness. It had demonstrated the competitive risk. A startup in Hangzhou, operating under US sanctions that restricted its access to the most advanced chips, had used Meta's openly shared research to build a model that rivaled Meta's own. If DeepSeek could do it, so could anyone. The moat that Meta was building through ecosystem dominance could be undercut by any sufficiently talented team willing to study the publicly available architecture and improve upon it.

This was the paradox at the heart of corporate open source, made vivid in a single event. Openness accelerates innovation — including innovation by your competitors. The question was whether the ecosystem benefits (developer loyalty, platform gravity, infrastructure lock-in) would outweigh the competitive costs. For Meta, the answer was about to become painfully unclear.

---

## The Unraveling

The sequence that followed was swift and brutal.

In April 2025, Meta launched the Llama 4 family of models — Scout and Maverick — with bold claims about performance. The company said its models outperformed GPT-4.5, Claude Sonnet 3.7, and Gemini 2.0 Pro on key benchmarks. The community was skeptical from the start, and within days the skepticism curdled into accusation. Researchers discovered that the version Meta had submitted to the LMArena benchmark leaderboard was not the same model it had released publicly. An "experimental" chat variant of Maverick, apparently optimized for the specific tests, had been used instead. [VERIFY: exact sequence of discovery]

Meta initially denied the allegations. But independent evaluations could not reproduce the company's claimed results. In third-party testing, Llama 4 underperformed its predecessor, Llama 3, on coding benchmarks. The gap between promise and reality was not a matter of interpretation. It was measurable.

The internal fallout was severe. Zuckerberg, according to reporting by The Information and others [VERIFY: primary source], lost confidence in the leadership of the GenAI organization and effectively sidelined the team responsible for the launch. Months later, Yann LeCun himself acknowledged that the benchmark results had been manipulated, describing them as having been "fudged a little bit."

Behemoth — the roughly two-trillion-parameter model that was supposed to be the crown jewel of the Llama 4 family — was postponed from its planned early summer release. Then postponed again, to fall. Then indefinitely. It never became generally available. The largest and most ambitious open-weights model Meta had ever attempted remained in "limited preview," a monument to ambitions that exceeded capabilities.

In June 2025, Zuckerberg made a move that signaled a fundamental strategic shift. Meta invested $14.3 billion for a 49 percent stake in Scale AI, and its founder, Alexandr Wang, left Scale AI to lead Meta Superintelligence Labs, an elite group of roughly fifty researchers that Zuckerberg had personally recruited at his homes in Lake Tahoe and Palo Alto.

The new lab was developing a model codenamed Avocado. And Avocado, according to multiple reports, might not be open source.

The irony was exquisite. The company that had positioned itself as open source's greatest corporate champion — that had hosted LlamaCon, published the manifesto, awarded the grants, built the ecosystem — was now funneling its most ambitious AI work into a proprietary lab led by an outside hire, developing a closed model that it hoped would catch up to Google, OpenAI, and Anthropic.

<!-- PP: The "Llamas to Avocados" CNBC headline from December 2025 is perfect. Consider using it as section title or at least referencing it. -->

By December 2025, the confusion was visible from outside the company. CNBC reported that Meta's shifting AI strategy was causing internal disarray, with engineers unsure whether the future was open or closed. Avocado's release, originally targeted for the first quarter of 2026, was postponed again. Internal tests reportedly showed it lagging behind the latest models from Google, OpenAI, and Anthropic. There were even reports that Meta had considered licensing Google's Gemini model as a fallback — the AI equivalent of admitting that your homegrown strategy had failed and you needed to buy from the competition.

The capital expenditure numbers told the story of escalating commitment. Meta's 2025 capex reached $70 to $72 billion, roughly eighty percent higher than the previous year. The guidance for 2026 was $115 to $135 billion. Zuckerberg projected at least $600 billion in US data center and infrastructure spending by 2028. These were not the budgets of a company confident in the efficiency of open-source development. They were the budgets of a company trying to brute-force its way to the frontier through sheer capital deployment.

---

## What the Reversal Reveals

Meta's arc from open-source champion to proprietary retreat is not a story of hypocrisy. It is a story about the structural limits of corporate open source — limits that have been present since the earliest chapters of this book but that the AI era has made inescapable.

The first limit is that corporate open source is conditional. Zuckerberg's letter was honest: he supported open source because it served Meta's strategic interests. When those interests shifted — when the open models failed to compete, when competitors exploited the openness, when the internal team lost credibility — the commitment evaporated. This is not a moral failing. It is the nature of corporate strategy. Companies optimize for survival and growth. Open source is a tool in that optimization, not a value that transcends it.

The second limit is that "open" is a spectrum, not a binary. Meta's Llama was never fully open by the standards of the organizations that define the term. It was open enough to build an ecosystem, open enough to generate goodwill, open enough to claim the mantle of openness in a corporate press release. But the training data stayed hidden, the license stayed restrictive, and the definition of "open source" was stretched until the OSI felt compelled to publicly object. When the pressure came, the company didn't move toward greater openness. It moved toward less.

The third limit is that the economics of AI may not support sustained openness. Red Hat could build a business on open-source software because the marginal cost of distributing code is zero and the value comes from services. But training a frontier AI model costs hundreds of millions of dollars in compute alone. When Meta was spending $70 billion a year on infrastructure, the calculus of giving everything away becomes harder to sustain — especially when the advertising revenue model, which made the original strategy viable, cannot scale fast enough to justify the investment.

The fourth limit — and the one that matters most for the remainder of this book — is that open source in AI creates risks that open source in traditional software did not. When Linus Torvalds released the Linux kernel, no one worried that it might be used to build autonomous weapons or generate synthetic propaganda at scale. The code was powerful, but its power was bounded by the physical systems it ran on and the human judgment that deployed it. AI models are different. Their capabilities are emergent, unpredictable, and increasingly autonomous. The question of whether to release them openly is not just a question of business strategy. It is a question of safety.

Meta's retreat from openness was driven by competitive failure, not safety concerns. But the retreat creates space for a different argument — one that other companies have been making with increasing urgency. The argument is that frontier AI models are too dangerous to release openly. That the risks of misuse, of weaponization, of loss of control, justify keeping the most powerful models behind closed doors. That openness, however valuable in software, becomes reckless in artificial intelligence.

This is the safety argument. And it is the subject of Part IV.

---

But before we arrive there, it is worth sitting with what Meta's confession reveals about the state of the freedom paradox at the threshold of the AI era. A company spent two years and billions of dollars building the most successful open-weights AI ecosystem in history. It generated 1.2 billion downloads, catalyzed 140,000 derivative models [VERIFY], attracted enterprise customers from Spotify to AT&T, and inspired a developer conference. Its CEO wrote the most candid public letter about corporate open-source strategy that any tech leader has ever produced.

And then, when the models underperformed, when a Chinese startup showed that openness cuts both ways, when the benchmarks turned out to have been manipulated, and when the capex bills climbed into the hundreds of billions — the company pivoted to proprietary development, hired an outside leader, built an elite lab, and started working on a closed model that it hopes will catch up to its competitors.

The ecosystem Meta built is real and will persist. Llama models will continue to be downloaded and deployed. The derivatives will multiply. The security tools and impact grants and API integrations will serve developers for years. Meta did not abandon open source entirely; it bifurcated its strategy, maintaining the open Llama line while developing Avocado behind closed doors.

But the confession has been amended. The original version said: we support open source because we learned what it means to be trapped by a closed platform. The amended version says: we support open source when it serves us, and we build proprietary systems when it doesn't.

This is not a betrayal. It is a clarification. And it is exactly the clarification that Part IV of this book will explore — applied not just to competitive strategy, but to the question of what happens when the technology itself becomes too powerful for the paradox to hold.

<!-- PP: Strong ending. The "confession has been amended" line is good. Make sure it lands. Consider whether the bridge to Part IV could be slightly shorter — you don't want to preview Ch10 so much that the reader feels they already know what's coming. -->
