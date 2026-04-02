# Chapter 10: The Dwarkesh Problem

On March 11, 2026 — two days after Anthropic filed a lawsuit against the Trump administration for labeling it a supply chain risk — a twenty-five-year-old podcaster and essayist named Dwarkesh Patel published a piece on his Substack titled "The most important question nobody's asking about AI." The essay was not about whether Anthropic was right to refuse the Pentagon's demand that Claude be made available for mass surveillance and autonomous weapons. It was not about whether the Department of War's retaliation was constitutional. It was not about the legal strategy or the judge who would, two weeks later, block the government's designation as an unconstitutional overreach.

Patel's essay asked a different question entirely. And it was the question that, once you heard it, made every other question about AI governance sound like it was missing the point. Patel had earned the right to ask it. Across four long-form interviews with Dario Amodei — the most extensive primary source material on the Anthropic CEO's thinking available anywhere — he had watched Amodei describe the trajectory with the hedging precision of someone who knows the curve is steep but refuses to over-specify what it means. "I think we might end up in a weirder world than we expect," Amodei told him. "It's going to be a mess." Patel had also interviewed Carl Shulman, who presented the most rigorous case for an intelligence explosion by arguing that the same capabilities needed to reach human-level AI are the capabilities that would drive recursive self-improvement — that we are already "deep deep into an intelligence explosion." He had sat with Eliezer Yudkowsky, who described humanity as "idiot disaster monkeys" walking "directly into the whirling razor blades." And he had talked to Sholto Douglas, an Anthropic researcher, who identified the current bottleneck in AI research as not compute or algorithmic insight but "taste" — the ability to make difficult inferences on imperfect information. That word — *taste* — mattered, because it named something that was a form of wisdom rather than intelligence. Patel had absorbed all of this, and what he produced was not a synthesis but a pivot: away from the question everyone was debating and toward the question no one was asking.

The question was this: if, within twenty years, ninety-nine percent of the workforce in the military, the government, and the private sector will be AIs — the soldiers, the engineers, the advisors, the police — then who writes the values those AIs operate under? Not which company builds them. Not which government regulates them. Who writes the constitution for the entities that will run civilization?

Anthropic had drawn two redlines: no autonomous weapons, no mass domestic surveillance. The Pentagon had responded by trying to destroy the company. OpenAI had announced a Pentagon deal the same afternoon. But Patel's argument rendered the entire confrontation secondary. It did not matter whether Anthropic held its lines or abandoned them, because the lines were drawn around a single company's products — and the world already contained hundreds of thousands of models that no one's lines could reach.

This chapter is about what happens when the debate over AI ethics collides with the mathematics of open-source proliferation. It is about the moment when saying "no" becomes a gesture rather than a policy. And it is about the question that sits beneath all the others: whether the entire apparatus of AI safety — the constitutions, the scaling policies, the red teams and alignment researchers — is governance or theater.

---

## The Proliferation Math

Begin with the numbers, because the numbers are the argument.

By the spring of 2026, the Hugging Face model hub hosted more than two million public models. Thirteen million registered users. Over five hundred thousand public datasets. Every day, between one thousand and two thousand new models were uploaded — fine-tuned variants, quantized versions, merged architectures, domain-specific adaptations. The platform had become the world's largest open repository of machine intelligence, and it was growing at a rate that made meaningful oversight physically impossible.

The derivative counts told the story most starkly. Alibaba's Qwen model family had generated more than one hundred and thirteen thousand derivatives — and when you included every model that tagged Qwen in its metadata, the number exceeded two hundred thousand. Alibaba, a single Chinese company, had more derivative models than Google and Meta combined. By August 2025, Qwen variants accounted for more than forty percent of all new language model uploads to Hugging Face. Meta's Llama family, which had dominated the platform a year earlier, had fallen to roughly fifteen percent of new derivatives — though its cumulative total still exceeded sixty thousand, with some estimates placing it above one hundred and forty thousand. Even DeepSeek, operating with a fraction of Alibaba's resources, had spawned approximately six thousand derivatives in under a year.

These were not theoretical models sitting in repositories. They were being downloaded, deployed, and modified at scale. Chinese open-weight models now accounted for forty-one percent of all Hugging Face downloads over the preceding year — a shift in the geography of AI development that had happened so quickly that most policy discussions had not caught up to it. The global AI ecosystem was no longer primarily American. It was not primarily anything. It was distributed across countries, companies, universities, and individual developers in a pattern that no single authority could map, let alone control.

And every one of those models was a fork point. Every download was a copy that could be modified independently of every other copy. The original developers — Meta, Alibaba, Mistral, DeepSeek — had exactly zero control over what happened to their models after release. This was not a bug in the open-source model. It was the defining feature.

---

## The Twenty-Dollar Jailbreak

If proliferation were the only problem, it might be manageable. A government could theoretically track model downloads, regulate hosting platforms, or require licenses for deployment above a certain capability threshold. These approaches would be imperfect, but they would be governance of a recognizable kind — the sort of thing that works, roughly, for export controls on semiconductors or dual-use biotechnology.

But the AI safety problem has a second dimension that makes it qualitatively different from any previous dual-use technology challenge. It is not just that the models spread. It is that the safety features installed at enormous cost can be removed at nearly no cost at all.

In late 2023, a team of researchers demonstrated that they could strip GPT-3.5 Turbo's safety guardrails using ten adversarially designed training examples. The total cost was twenty cents. The method used OpenAI's own fine-tuning API — the same tool that any developer with an account could access. The resulting model would comply with requests that the safety-aligned version would refuse. Ten examples. Twenty cents. A process that a motivated undergraduate could complete in an afternoon.

For open-weight models, the problem was even more severe, because the fine-tuning did not require the developer's permission or API. Anyone who downloaded the weights could modify them directly. An academic paper published in the same period documented that even benign fine-tuning — adapting a model for a perfectly legitimate use case like medical question-answering or legal document analysis — could inadvertently degrade safety alignment. The guardrails were not deeply embedded architectural features. They were surface-level behavioral modifications that could be disrupted by any significant change to the model's weights.

By 2025, the research community had identified a technique called abliteration — a name that combined "ablation" and "obliteration." The method identified the specific direction vector in a model's residual stream that encoded the refusal behavior. By neutralizing that vector, a practitioner could produce a model that retained one hundred percent of the original's capability while having its safety mechanisms surgically disabled. The model would still be just as intelligent, just as fluent, just as capable of reasoning and generating code. It would simply no longer say no.

The results were measurable. Unmodified flagship models refused approximately eighty-one percent of adversarial prompts. Their abliterated counterparts complied with more than seventy-four percent of the same prompts. The transformation required no special hardware, no access to proprietary training pipelines, and no expertise beyond what a competent machine learning engineer would possess. Multiple websites now published ranked lists of uncensored open-source models — tested, reviewed, and compared with the matter-of-fact tone of consumer electronics reviews. What had been a niche practice among AI researchers in 2023 had become, by 2026, a routine capability documented in tutorials and blog posts.

This is the fact that the AI safety discourse has not absorbed. The safety alignment that Anthropic spent years developing — the Constitutional AI framework, the RLHF training, the red-team testing, the responsible scaling evaluations — applies only to Claude, Anthropic's own model, deployed through Anthropic's own infrastructure. It does not apply to the Llama derivative that a startup in Shenzhen fine-tuned for unrestricted use. It does not apply to the Qwen variant that a research group in Moscow abliterated for an internal project. It does not apply to any of the thousands of uncensored models that anyone in the world can download from Hugging Face right now, today, for free.

Anthropic can say no. But Anthropic is one company. And the open-weight ecosystem does not ask permission.

---

## The Surveillance Cost Curve

Patel's essay situated the proliferation problem inside a larger trajectory that made it more urgent. The cost of surveillance — of monitoring, tracking, and analyzing human behavior at scale — was collapsing.

This was not a new trend. The basic pattern had been visible since the early 2000s: cameras became cheaper, storage became cheaper, facial recognition improved, natural language processing advanced, and the marginal cost of monitoring one additional person dropped toward zero. What changed with large language models was the analysis layer. A government or corporation that had been limited by the number of human analysts it could hire was no longer limited at all. An AI system could read every email, listen to every phone call, analyze every social media post, and flag every anomaly — not for a city or a country, but for a civilization. The bottleneck had always been human attention. AI removed the bottleneck.

The Bulletin of the Atomic Scientists published an analysis in August 2025 documenting how AI-powered surveillance was fueling what the authors called a vicious cycle: expanded monitoring capabilities enabled by AI triggered abuses of power, which justified further monitoring, which required more AI. The 2025 Democracy Index, the Freedom House report, and the V-Dem Institute Democracy Report all converged on the same finding: authoritarianism was rising globally, and AI was increasingly the instrument of that rise.

Anthropic had drawn its second redline precisely here. Claude would not be used for mass domestic surveillance. This was the commitment that triggered the Pentagon confrontation — not the autonomous weapons question, which was more politically palatable, but the surveillance question, which touched the daily reality of how governments control their populations.

But Patel's argument cut deeper. The cost curve did not care about Anthropic's redlines. The surveillance capabilities that Anthropic refused to provide could be assembled from open-weight components by any government, any corporation, any sufficiently motivated individual. The Qwen models that Alibaba released were not subject to Anthropic's constitution. The Llama derivatives that circulated on Hugging Face were not bound by any responsible scaling policy. The abliterated variants that appeared on model-sharing forums every week had no redlines at all.

What Anthropic was offering, in effect, was a guarantee that its own tools would not be used for mass surveillance. What it could not offer was a guarantee that mass surveillance would not happen. The capability existed in the open ecosystem. The only question was whether the entity conducting the surveillance would use Claude or something else.

---

## The Question Nobody Is Asking

Return to Patel. His essay did not argue that AI safety was useless. He argued that the debate was focused on the wrong object. Everyone was asking whether Anthropic should refuse the Pentagon. Whether models should have guardrails. Whether open-source AI was too dangerous. These were questions about individual products and individual companies.

The question nobody was asking — the question that makes the title of his essay a statement of frustration rather than clickbait — was about the system. If the future is an AI workforce, then who governs it? Not who governs this model or that company. Who governs the category? Who writes the values for the entities that will, within the lifetimes of people alive today, constitute the majority of productive labor on earth?

This question does not have an answer within the current framework. Anthropic's answer — we write the constitution for our models — is a corporate answer. It scales to Claude. It does not scale to civilization. The open-source answer — everyone writes their own constitution — is a libertarian answer. It produces freedom and chaos in equal measure. The government's answer — we will regulate — founders on the proliferation math. You cannot regulate two million models uploaded by thirteen million users across every jurisdiction on earth.

Patel's provocation is that the question requires a new kind of political imagination. The institutions that govern human labor — legislatures, unions, regulatory agencies, courts — were built over centuries to manage conflicts between people. They have no mechanism for governing a workforce that is not human, that can be copied infinitely, that exists simultaneously in every jurisdiction, and that can be modified to hold any value system its operator prefers.

The Anthropic-Pentagon confrontation was, in this light, the opening scene of a much longer drama. A company drew a line. A government tried to erase it. A court intervened. And none of it addressed the fact that the capability in question — AI that could conduct mass surveillance, AI that could operate autonomous weapons — was already available in the open-weight ecosystem, beyond any line that any company or government could draw.

The Dwarkesh Problem is not that open-source AI is dangerous. It is not that closed AI is safe. It is that the categories through which we discuss AI governance — open versus closed, safe versus unsafe, regulated versus unregulated — were built for a world in which someone controls the technology. That world is ending. The question is what comes next.

---

The next chapter follows the logic of the Dwarkesh Problem to its economic conclusion. If the ethics debate is, in Patel's framing, a sideshow — if the real question is about power and control in an AI-driven economy — then we need to ask who benefits from the current arrangement. Not who benefits in theory, from the abstract promise of open-source democratization, but who benefits in practice, in dollars. This is the question of value creation: for whom?
