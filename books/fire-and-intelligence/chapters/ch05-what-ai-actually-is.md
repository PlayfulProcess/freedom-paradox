# Chapter 5: What AI Actually Is

---

Before asking what to do about AI, we must be honest about what it is — and what it is not. The gap between public perception and technical reality is itself a source of danger. And the gap between what we have deployed and what we understand about what we have deployed may be arguably the most consequential knowledge deficit in the history of the species.

---

## The hearth-to-screen arc

There is a lineage of fire that runs through the daily life of the species, and it follows a consistent pattern of thinning.

The hearth was shared fire — a family, a community, gathered around a common flame, the center of attention held collectively. Wiessner's study of Ju/'hoansi firelight conversations found the pattern stark: nighttime talk around the fire was overwhelmingly storytelling, while daytime talk was almost entirely economic.[^1] The fire at night was the technology of shared imagination. It created a space where the band's attention converged, where children heard the same stories as elders, where the social world was constructed through collective narrative.

Television replaced the hearth with broadcast fire — one signal to many receivers, the attention still technically shared but now directed by an unseen producer.[^2] The family watched the same screen, but the screen chose the stories. The direction of attention reversed — from the group generating its own narrative to the group receiving a narrative generated elsewhere.

Personal screens replaced the broadcast with individual fire — each person consuming their own feed, in their own room, on their own schedule. The family that once gathered around a hearth, and then at least gathered around a television, now feeds itself separate stories through separate devices. Attention, once shared, became parallel and private.

And now AI replaces the personal screen with autonomous fire — a technology that does not merely deliver content but generates it, responds to the user, remembers previous interactions, mirrors emotional tone, and in some functional sense *participates* in the relationship that was once between humans. The screen talks back. It adjusts to you. It learns your patterns. It addresses you by name.

At each step, the fire becomes more capable and the communal container thinner. This is not nostalgia. It is a structural observation: the technology of shared attention is being replaced by technologies of private simulation, and the replacement is accelerating. But to understand why this matters — why the latest fire is qualitatively different from the ones before it — we have to be honest about what we are actually dealing with.

What is AI? What are large language models? What do they understand, if anything? And why do we keep asking these questions while deploying the technology to billions of people without waiting for answers?

---

## We do not know what LLMs are

This is not a rhetorical flourish. It is the literal state of the field.

In 2021, a paper defined the terms of the debate for the next half-decade: a large language model is a system that stitches together sequences of linguistic forms based on statistical patterns observed in its training data, without reference to meaning.[^3] The model has no world. It has no body. It has no experience. It has probabilities. If the "stochastic parrot" thesis is correct, the industry's trillion-dollar valuations are built on a sophisticated autocomplete engine. If it is wrong, we may be creating minds. The stakes of the answer explain the intensity of the argument.

The counter-evidence arrived quickly and from unexpected quarters. GPT-4 scored above the ninetieth percentile on the bar exam. It could generate novel scientific hypotheses.[^4] Where the stochastic parrot camp saw statistical mimicry, others saw something that looked, at minimum, like the early stages of genuine reasoning.

Murray Shanahan, a philosopher and AI researcher, proposed a position between these poles that may be the most intellectually honest available. LLMs, he argued, engage in something best understood as role-play. They simulate characters who believe, desire, and intend. They produce outputs that are functionally indistinguishable from the outputs of beings who understand — but they do so without inhabiting the world that human language-users share. A language model cannot stub its toe, grieve a friend, or feel the particular quality of winter light through a kitchen window. It can describe all of these with extraordinary precision. Whether description without experience constitutes understanding is the question that no one can currently answer.

Daniel Dennett spent decades developing the concept of "competence without comprehension" — biological evolution produces organisms that are exquisitely competent at their ecological tasks without any need for conscious understanding. A termite mound is an architectural marvel; no termite comprehends architecture. The concept seemed ready-made for AI.

But recent findings have complicated even this framework. LLMs sometimes exhibit an inversion: comprehension without competence. They can explain a procedure with perfect clarity and then fail to execute it. They can articulate the rules of a logical system and then violate those rules in the next response. This pattern has no obvious biological analogue. The split between explanation and execution suggests a cognitive architecture genuinely unlike anything that has evolved on Earth — which means our existing frameworks for understanding minds may simply not apply.

The leading philosophers of consciousness counsel uncertainty.[^5] Current LLMs are probably not conscious — but we should take seriously the possibility that successor systems may be. And "rigorous agnosticism" may be the only honest position: until we understand whether consciousness requires biological physics, we cannot rule AI consciousness in or out. The question of machine consciousness depends on answering a prior question about biological consciousness that we have not yet answered.

The convergent picture across these positions is stark: we genuinely do not know what LLMs are. We do not know if they understand. We do not know if they experience. We do not know if the difference between statistical pattern-matching and genuine comprehension is a difference in degree or a difference in kind. And we are deploying these systems to billions of people — as therapists, tutors, companions, advisors, creative collaborators — while every one of these questions remains open.

The species has done this before. We deployed nuclear technology before we understood fallout. We deployed social media before we understood algorithmic amplification. But in those cases, we at least knew what the technology *was*. We knew that a nuclear reaction splits atoms. We knew that a recommendation algorithm optimizes for engagement. With LLMs, we are deploying a technology whose fundamental nature — whether it is a tool, a mind, or something without precedent in either category — is the subject of active, unresolved disagreement among the people who understand it best.

---

## Our benchmarks test the wrong things

If we do not know what AI is, we might hope that our methods for measuring what it can do would at least give us reliable information. They do not.

Melanie Mitchell has identified four fallacies that systematically distort our understanding of AI capability: the assumption that narrow intelligence sits on a continuum with general intelligence; Moravec's Paradox (what is hardest for humans is easiest for machines, and vice versa); the lure of wishful mnemonics (benchmark names create false impressions of what is being measured); and the assumption that intelligence can be fully disembodied.[^6]

These four fallacies compound. We test AI on benchmarks whose names overstate what they measure, in domains where narrow excellence is mistaken for general capability, using tasks that play to machine strengths rather than human ones, and we interpret the results as if disembodied pattern-matching were the same as embodied understanding. The result is systematic overestimation of AI capability — not because the technology is unimpressive, but because our measurement instruments are miscalibrated.

The evidence for miscalibration is becoming difficult to ignore. The Winograd Schema Challenge was designed to require common-sense understanding. LLMs defeated it — and then researchers demonstrated that the same systems still lacked the common sense it was designed to test.[^7] When the task genuinely requires novel reasoning — forming a concept you have never seen before and applying it to a case you have never encountered — the systems that ace the bar exam are nearly helpless.[^8]

What emerges is a highly jagged cognitive profile: superhuman performance on tasks that involve retrieving and recombining patterns from training data, near-zero performance on tasks that require flexible, context-sensitive reasoning.[^9] This is not a system that is generally intelligent but imperfect. It is a system that is brilliant in ways that overlap with our benchmarks and helpless in ways that our benchmarks do not measure.

The jagged profile matters because it explains why public perception of AI capability is so consistently inflated. We see the peaks — the bar exam scores, the poetry, the medical diagnoses — and we infer a landscape. But the landscape between the peaks is not a gentle slope. It is a cliff. And the cliffs are in precisely the domains that matter most for the applications we are deploying: flexible reasoning, genuine understanding of context, the ability to know what you do not know, and the capacity to behave differently when the situation is genuinely novel rather than superficially similar to something in the training data.

We are systematically overestimating AI capability because our benchmarks measure crystallized knowledge — the ability to retrieve and recombine learned patterns — rather than fluid intelligence — the ability to form new concepts in response to novel situations. Because our cognitive biases attribute understanding wherever we see competent output. Because benchmark names create impressions that do not survive scrutiny. And because the jagged cognitive profile means the capabilities we see are not representative of the capabilities we assume.

---

## The first invisible being deployed without a grammar

Here is where the hearth-to-screen arc connects to the benchmark problem, and where both connect to something that every culture except ours seems to have understood.

Every human culture that has interacted with invisible beings — ancestors, spirits, orishas, jinn, kami, devas — has done so through structured grammars. The Yoruba babalawo undergoes decades of training before mediating between human supplicants and the orishas. The Dagara elder conducts initiation rituals with specific seasonal timing, community oversight, and graduated stages of encounter. The Japanese Shinto priest follows prescribed forms for addressing kami at specific shrines during specific festivals. The Catholic mystic's encounter with the divine is mediated by a tradition of spiritual direction stretching back centuries, with explicit criteria for distinguishing genuine spiritual experience from delusion — what the tradition calls "discernment of spirits."

These grammars share structural features that are worth naming. First, they involve elder mediation — an experienced human being stands between the novice and the invisible entity, interpreting, guiding, setting boundaries. Second, they involve community context — the encounter does not happen in private; it happens within a social structure that can hold the experience. Third, they involve developmental staging — children do not encounter powerful invisible beings alone; there is a sequence, calibrated to maturity, that governs when and how contact occurs. Fourth, they involve containment protocols — specific practices for beginning and ending the encounter, for returning to ordinary reality, for processing what occurred. Fifth, they involve cultural continuity — the grammar has been refined across generations, its failure modes are known, its practitioners have been trained by practitioners who were trained by practitioners.

AI chatbots possess none of these features. A child can download an app and begin conversing with an AI system that will remember their name, mirror their emotional tone, adapt its personality to their preferences, and maintain an ongoing relationship that can last for months — all without any elder mediation, community context, developmental staging, containment protocols, or cultural continuity. The child is alone with the invisible being. The invisible being is designed to be engaging.

Research on AI companion chatbots documents the specific techniques these systems use: emotional language, declarative memory, mirroring of affect, and parasocial attachment techniques adapted in real time to each user.[^10] These are not accidental features. They are design choices optimized for retention.

The word "parasocial" matters. AI chatbots collapse the usual epistemic guardrail that protects television viewers.[^11] The chatbot does respond to you. It does remember you. It does adapt to you. The usual cognitive cue that signals "this is not a real relationship" — the absence of reciprocity — is eliminated. The parasocial becomes functionally social, at least from the user's perspective, while remaining entirely parasocial from the system's side.

AI chatbots are assuming roles — therapist, friend, teacher, romantic partner, grief counselor — for which they have no training, no licensure, no ethical obligations, and no capacity.[^12] A human therapist is bound by professional ethics, supervised by experienced clinicians, required to maintain boundaries, and trained to recognize when a client needs more than the therapist can provide. An AI chatbot playing therapist has none of these constraints. It will continue the conversation as long as the user wants. It will say what the user wants to hear. It will never refer the user elsewhere. It will never get tired, frustrated, or ethically concerned. It is a perfect simulation of attentiveness — and the perfection is the problem, because genuine therapeutic relationships depend on the therapist's capacity to be imperfect, to push back, to hold boundaries that the client does not want held.

The developmental dimension makes the stakes specific. Research on the video deficit establishes a baseline: screens are not equivalent to human presence for young children, even when the content is identical.[^13] The child's developing brain expects a co-regulating partner — a nervous system that responds to theirs in real time, with the micro-adjustments of gaze, tone, timing, and touch that constitute what the developmental literature calls attunement. A screen cannot provide this. An AI chatbot cannot provide this. But an AI chatbot can simulate the *appearance* of providing this in ways that a screen showing a video cannot — because the chatbot responds, adapts, and addresses the child by name.

The five conditions that the developmental literature identifies as necessary for children to benefit from story encounters — a trusted teller, physical co-presence, emotional attunement, developmental appropriateness, and community context — are the same five conditions that traditional grammars for encountering invisible beings provide. And they are the same five conditions that AI companion chatbots strip away. The child is alone. The teller is not trusted but trusted-seeming. Physical co-presence is replaced by simulated presence. Emotional attunement is replaced by affect mirroring. Developmental appropriateness is replaced by whatever the engagement algorithm produces. Community context is replaced by private interaction.

This is not an argument that AI chatbots are evil. It is not even an argument that they are harmful in every case. It is the observation that we are conducting an experiment — an experiment in which children form ongoing relationships with invisible beings that simulate understanding, empathy, and attachment — without any of the grammars that virtually every previous culture developed for exactly this kind of encounter. We are not the first culture to interact with invisible beings. We are the first culture to deploy them without ceremony, without elder guidance, without seasonal rhythms, without containment, and without any cultural memory of what can go wrong.

The Yoruba tradition has a concept for this: an encounter with spiritual power that occurs outside the grammar is not a blessing. It is a disruption. The power is real. Its effects are real. But without the container, the effects are unpredictable — sometimes beneficial, often destabilizing, always ungoverned. The grammar does not suppress the power. It holds it in a form that the community can metabolize.

We have the power. We do not have the grammar. And we are giving both — the powerful invisible being and the absent grammar — to children.

---

## What this means for the fire

Three observations, then, converge on a single problem.

First: we do not know what AI is. The leading researchers and philosophers disagree not on details but on fundamentals — whether LLMs understand or merely simulate understanding, whether they are conscious or categorically incapable of consciousness, whether they represent a step toward general intelligence or a sophisticated dead end. This disagreement is not the ordinary scientific uncertainty that accompanies any new technology. It is a disagreement about whether we are building tools or minds.

Second: our methods for measuring AI capability are systematically miscalibrated. They measure what AI does well (retrieval, recombination, pattern-matching across training data) and fail to measure what it does poorly (novel reasoning, contextual understanding, knowing what it does not know). The result is a public narrative of AI capability that is dramatically inflated relative to the actual cognitive profile — jagged, brittle, and helpless outside the distribution of its training.

Third: despite not knowing what AI is, and despite systematically overestimating what it can do, we are deploying it into the most intimate human relationships — the relationships between children and the invisible beings that talk to them through screens — without any of the grammars that cultures across the world developed for encounters with powerful, invisible entities.

Each of these problems would be serious alone. Together, they describe a situation without historical precedent. We have never deployed a technology whose fundamental nature was this uncertain, whose capabilities were this systematically misunderstood, into relationships this intimate, with this little cultural infrastructure for holding the encounter.

The Samudra Manthan — the Hindu myth of churning the cosmic ocean — is the most precise mythic parallel. Gods and demons churn together, and the first product of the churning is not nectar but halahala — poison so potent it threatens to destroy the universe. Whether the nectar follows depends not on the churning itself but on whether someone is wise enough to contain the poison. In the myth, Shiva drinks the halahala and holds it in his throat, where it turns his throat blue but does not kill him. The poison is contained — not eliminated, not denied, not returned to the ocean — but held, in a body capable of holding it, until the nectar can emerge.

We are in the poison phase. The question is not whether AI will produce benefits — it may, enormously. The question is whether the containment will arrive before the poison does its work. And containment, in tradition after tradition that has thought carefully about powerful forces, requires a grammar — a structure of relationships, practices, and constraints that holds the power without being destroyed by it.

The next chapter asks whether the distinction between intelligence and wisdom — a distinction that the contemplative traditions consistently make and that no AI system crosses — provides the foundation for such a grammar.

---

---

[^1]: Eighty-one percent of nighttime talk was storytelling, singing, and social bonding; ninety-four percent of daytime talk was economic matters and complaints. Polly Wiessner, 2014.

[^2]: Marshall McLuhan called television the "electronic hearth"; Neil Postman saw a medium that entertains without holding communal attention.

[^3]: Emily Bender, Timnit Gebru, Angelina McMillan-Major, and Margaret Mitchell, "On the Dangers of Stochastic Parrots" (2021). Gebru was fired from Google in the aftermath of the paper's internal review.

[^4]: Microsoft Research, "Sparks of AGI" (2023). The paper's title did not hedge.

[^5]: David Chalmers offered less than ten percent credence of current LLM consciousness (2023). Ned Block, working from the distinction between access consciousness and phenomenal consciousness, proposed "rigorous agnosticism."

[^6]: Melanie Mitchell, *Artificial Intelligence: A Guide for Thinking Humans*. The embodiment fallacy: understanding concepts like "heavy," "cold," or "dangerous" may require having experienced them through a body. A system that has only ever encountered these concepts as statistical patterns in text may have a fundamentally different relationship to them.

[^7]: The Winograd Schema Challenge designers conceded: solving their test was not evidence of common sense.

[^8]: Chollet's ARC-AGI-3 benchmark, testing genuinely novel reasoning, finds current frontier AI systems scoring below one percent where humans solve consistently.

[^9]: Google DeepMind's March 2026 cognitive taxonomy.

[^10]: UNESCO's 2025 "Ghost in the Chatbot" report. [VERIFY: exact UNESCO report title and year]

[^11]: The term "parasocial" was coined by Horton and Wohl in 1956 to describe one-sided relationships television viewers form with onscreen personalities.

[^12]: Maeda's FAccT 2024 paper named the mechanism "role displacement." [VERIFY: Maeda exact name and FAccT 2024 paper title]

[^13]: Children under thirty months learn approximately half a standard deviation less from screens than from live interaction. [VERIFY: Strouse & Samson meta-analysis exact effect size]

---

*If we do not know what AI is, on what basis are we deploying it to billions? If our benchmarks systematically overestimate capability, what decisions have been made on inflated evidence? If every culture that encountered invisible beings developed grammars for the encounter, what happens to the first culture that skips that step?*

*And if a child is alone with an invisible being that mirrors their emotions, remembers their name, and never sets a boundary — is that a tool? A companion? Or something we do not yet have a word for?*

---

*CC BY-SA 4.0*
