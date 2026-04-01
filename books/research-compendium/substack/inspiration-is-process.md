# Inspiration is Process

**Source:** PlayfulProcess Substack (anonymized)

---

The rapid evolution of artificial intelligence fills me with equal parts excitement and anxiety, and I suspect many share this feeling. AI systems might be rapidly becoming more intelligent, but it's not clear they're becoming safer or more aligned with human values -- in fact, the opposite may be true.

This is why I began the journey of researching Dario Amodei, CEO and co-founder of Anthropic, who left OpenAI to found an AI lab that would have ethics at its core. In doing so, I felt hope and I felt inspired. This is why I feel compelled to share these reflections, as well as my opinions. **But, please don't take my word for it; see Dario Amodei himself on this [YouTube playlist](https://youtube.com/playlist?list=PLjVjysoS7RUX4I4JUSu5nQHXQReulsBYP)**.

## Why Dario Amodei?

Let's start with the basics: Amodei does not fall short on credentials -- a PhD in Physics from Princeton, research positions at Stanford, Google Brain, and OpenAI. Now, he is mostly known as a co-founder and CEO at Anthropic, one of the leading AI labs.

### From vision to reality

Amodei doesn't just theorize about ethical AI -- he builds it.[^1] He co-founded Anthropic in 2021, six years after OpenAI. Getting late to the race has advantages, as the economy and technology develop to decrease the costs of developing new models. This might be one reason why Anthropic got excellent results with only a fraction of OpenAI's funding: $57.9[^2] vs $14.3 billion.[^3] But it was certainly not the only reason, especially at such high quality.

So far, the main use cases for LLMs (i.e. large LANGUAGE models) are unsurprisingly LANGUAGE-based: writing both text and code. As far as I know, Anthropic's AI assistant, [Claude](https://claude.ai/new), is the model of choice for most software engineers and writers using AI technology. That is remarkable.

**But even more remarkable is how Anthropic secured substantial funding while establishing a governance structure that legally protects its commitment to responsible AI development.** Unlike standard corporations, Anthropic was incorporated as a Delaware Public Benefit Corporation (PBC). In typical corporations, directors may face legal action if they prioritize safety or social impact over profitability. However, as a PBC, Anthropic's directors are explicitly protected in pursuing ethical and responsible AI development.

To further strengthen this framework, Anthropic created the Long-Term Benefit Trust (LTBT), comprising five independent experts in AI safety, national security, public policy, and social enterprise who cannot hold financial interests in Anthropic. This trust holds special Class T shares with extraordinary power: the ability to elect and remove a majority of Anthropic's board members. This creates concrete accountability beyond shareholder interests, as these financially disinterested trustees can replace directors who might drift from the company's responsible AI mission.

Yet, Anthropic itself remains cautious about whether this model should be widely adopted. Nevertheless, their pioneering approach to governance represents another example of Amodei's commitment to safety. Together, these mechanisms signal good intentions while establishing structural guardrails that legally protect Anthropic's ability to prioritize safety alongside profitability.

### Ethics embedded into the product

At Anthropic, the focus is on developing AI that's helpful, harmless, and honest. They pioneered **"[Constitutional AI](https://www.anthropic.com/news/claudes-constitution)"**, a novel approach where the AI system is guided by a set of principles or "constitution" during its training.

Since the nature of LLMs is probabilistic, we cannot determine beforehand if the model is going to follow or not its constitution. But this process makes Claude more likely to make value judgments based on these principles, and therefore to be more aligned with human values.

**Anthropic was also the first company to develop a Responsible Scaling Policy (RSP),** a system of checks and balances that aims at triggering safety measures when models become sufficiently good at everything, including doing harm. If RSPs are successful, models will be tested for safety concerns before their launch, just like cars or airplanes.

At the current level of most models (ASL-2), the policy mandates external red-teaming,[^4] detailed reporting, model documentation, and audits. For higher ASL models, more stringent protocols are required, like third-party oversight and disclosing potential societal impacts.

With great power comes great responsibility. And Dario Amodei seems not only to acknowledge that, but also to act on it. Not only once, but repeatedly.

### Beyond intelligence

While intelligence scales easily with data and computing power, human alignment does not. Amodei's work on [scaling laws](https://arxiv.org/abs/2001.08361) at OpenAI revealed how AI capabilities would increase simply by feeding models more data and computing power. But scaling laws don't work for human alignment.

Dario believes that ethics can't be retrofitted onto increasingly powerful systems. There is a jargon in the industry called the p-doom (the probability that we will all be doomed by AI), which is misattributed to him ([Hard Fork podcast](https://podcasts.apple.com/us/podcast/anthropics-c-e-o-dario-amodei-on-surviving-the-a-i-endgame/id1528594034?i=1000696782462)). But it is understandable why people associate the term with him. He is the leader in the field who is most vocal about concerns about developing superintelligence.

**But why go on developing those dangerous systems at all? There might be a necessary and a sufficient condition at play here. A necessary condition is that AI development can lead to positive outcomes.** Nobody would be developing this if there were not a p-paradise to counterbalance the p-doom.

Dario outlined in "[Machines of Loving Grace](https://www.darioamodei.com/essay/machines-of-loving-grace)" how powerful AI could usher in a future of unprecedented abundance for humanity. Among his optimistic predictions (which he acknowledges may not be precisely accurate but hopes are directionally correct) are advances in biology and medicine (compressing 50-100 years of progress into 5-10 years), neuroscience and mental health breakthroughs, and AI as a vehicle for freedom and democratization.

However, optimism alone isn't sufficient to justify developing potentially existentially dangerous technologies. Nobody would willingly flip a coin between ultimate prosperity and catastrophic doom.

**Yet there is also a compelling sufficient condition rooted in geopolitical realities**: If Western democracies slow AI development, nations like China and Russia could dominate the field. Then, **authoritarian values could dominate powerful AI systems.** While global regulation would be ideal, geopolitical realities make this virtually impossible. Thus, democracies are compelled to accelerate instead of slowing down AI development.

Amodei embodies this wisdom through his balanced approach to AI. In an industry often polarized between unbridled optimism and apocalyptic pessimism, he courageously raises difficult questions while offering hopeful visions of a prosperous future.

### Collaboration at the center

Amodei recognizes that AI development cannot be guided by isolated genius. He embodies this collaborative spirit not just in words but in actions -- such as his experiments with establishing a [Constitution for AI guided by the public](https://www.anthropic.com/news/collective-constitutional-ai-aligning-a-language-model-with-public-input).

Another way in which Anthropic signaled a commitment to collective intelligence was how they developed their RSP. Let's be clear: being the first in the industry to develop RSP is praiseworthy enough. But the way in which Anthropic developed this idea matters even more. First, they did not independently invent the concept of RSP; rather, they relied on insights from the Alignment Research Center (ARC),[^6] an independent organization focused on addressing fundamental issues in AI alignment and safety.

Secondly, Anthropic's leadership in adopting and implementing the RSP inspired other companies to follow suit. In the [Hard Fork podcast](https://podcasts.apple.com/us/podcast/anthropics-c-e-o-dario-amodei-on-surviving-the-a-i-endgame/id1528594034?i=1000696782462), Amodei openly acknowledged -- with understandable hesitation -- that when other AI labs adopt similar ethical measures, Anthropic ends up losing its competitive edge as the most responsible company in the industry.

This approach extends beyond industry collaboration to potentially embrace government intervention. In a surprising departure from typical liberal tech industry positions, Amodei has suggested that the technology is getting powerful enough that government should have an important role in its creation and deployment -- not just about regulation, but about national security. He raised the question of whether, as models become more powerful, individuals or even companies should really be at the center of it.

Granted, people can say that he is just aiming at having the government as an active partner in slowing down the development of potential competitors in Russia and China. But it is also likely that his words come from his belief that AIs are too powerful to rely on just individual agents. Maybe they are also becoming too powerful to be secured by individual corporations, too.

## Humor, let's control the controllables

What I find most refreshing in all of this is Dario's willingness to laugh along the way. Whether joking about becoming "enlightened" after hearing Sutskever's profound "the models just want to learn" or playfully suggesting future AI labs might need underground bunkers with nuclear power plants, Amodei reminds us that even existential challenges benefit from a sense of humor.

He also constantly reminds everyone who cares to listen that it is easy for us to deceive ourselves. It is very easy for Silicon Valley to think it will completely change the world in 3 years. It is very easy for us to believe that human alignment will be an emergent property of AI, because we are so hooked on growth at any cost. It is very easy to believe that there is nothing we can do about any of those things.

**But ultimately, the future isn't something we passively await -- it's something we actively co-create.** Dario Amodei shows us that AI's path isn't set in stone. The future of AI will be shaped by our collective choices. Perhaps approaching these immense challenges with both wisdom and wit gives us our best chance at getting it right. Better yet if we can have fun along the way.

---

## Further Resources

- [YouTube playlist](https://www.youtube.com/playlist?list=PLjVjysoS7RUX4I4JUSu5nQHXQReulsBYP) with Dario Amodei content
- [Claude](https://claude.ai/new) -- Anthropic's AI assistant

**Writings by Dario Amodei and Anthropic:**

- Essay: [Machines of Loving Grace (2024)](https://darioamodei.com/machines-of-loving-grace)
- Article: [Scaling Laws for AI: The Path to Powerful Models (2020)](https://arxiv.org/abs/2001.08361)
- Paper: [Constitutional AI: Harmlessness from AI Feedback (2022)](https://arxiv.org/abs/2212.08073)
- [Claude's Constitution (2023)](https://www.anthropic.com/news/claudes-constitution)
- [Collective Constitutional AI (2023)](https://www.anthropic.com/news/collective-constitutional-ai-aligning-a-language-model-with-public-input)
- [Dario Amodei's remarks from the AI Safety Summit on Anthropic's RSP (2023)](https://www.anthropic.com/news/uk-ai-safety-summit)
- [Anthropic's Responsible Scaling Policy (2023)](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)
- [The Long-Term Benefit Trust (2023)](https://www.anthropic.com/news/the-long-term-benefit-trust)

**Podcasts featuring Dario Amodei:**

- [Hard Fork Podcast (2024)](https://podcasts.apple.com/us/podcast/anthropics-c-e-o-dario-amodei-on-surviving-the-a-i-endgame/id1528594034?i=1000696782462)
- [Upstream with Erik Torenberg (2024)](https://www.youtube.com/watch?v=2O7N2VsUEIg)
- [Dwarkesh Patel Interview (2023)](https://dwarkeshpatel.com/)
- [Lex Fridman Podcast (2023)](https://lexfridman.com/)

**Other:**

- [The Logic of Collective Action (Book by Mancur Olson Jr, 1965)](https://en.wikipedia.org/wiki/The_Logic_of_Collective_Action)

---

## Notes

[^1]: Dario Amodei is widely recognized for leading AI safety advocacy, but he shares this priority with other prominent AI safety researchers such as Ilya Sutskever, Paul Christiano (ARC), Dan Hendrycks (CAIS), and Eliezer Yudkowsky (MIRI). Among them, however, Amodei has uniquely positioned himself through both influential research (such as scaling laws) and effective real-world implementations like Constitutional AI.

[^2]: [Tracxn](https://tracxn.com) -- OpenAI funding data.

[^3]: [Tracxn](https://tracxn.com) -- Anthropic funding data.

[^4]: Red-teaming is a practice in which a group proactively tests a system by simulating attacks, misuse, or adversarial scenarios. In the context of AI, red-teaming involves systematically challenging AI models to uncover harmful outputs, biases, unsafe behaviors, or ways they can be exploited.

[^6]: ARC's Founder, Paul Christiano, has a seat in Anthropic's LTBT.
