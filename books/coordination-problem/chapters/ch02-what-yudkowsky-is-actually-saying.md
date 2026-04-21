# Chapter 2: What Yudkowsky Is Actually Saying

---

Before a claim can be evaluated, it has to be stated. Yudkowsky's claim, in the form most people have encountered it, is a *TIME* op-ed calling for airstrikes on datacenters. This is what he said. It is not all he said. It is not even the load-bearing part of what he said. It is the tail of an argument whose beginning most readers never encountered.

This chapter is that argument, stripped. Not persuaded of. Not dismissed. Stated.

I will use Yudkowsky as the focal voice because he has been the clearest and most uncompromising about the version of the case I want to examine. But the argument does not belong to him alone. Nate Soares, his co-author, has been making it alongside him for years. Paul Christiano has been making a more moderated version of it from inside the technical alignment community. Stuart Russell has been making a policy-register version of it from academia. Bengio has been making a cautious-senior-scientist version of it. The argument has a shape that is larger than any one person making it.

Here is that shape.

---

## Claim 1: We do not know how to build systems more capable than us that reliably do what we want.

Start with the word *alignment*. In AI research it means, roughly, the problem of getting a system to do what its designers intended, in a robust way, across situations the designers did not anticipate.

For current large language models, alignment is mostly done by a technique called reinforcement learning from human feedback — RLHF. The basic idea: after pretraining on a huge text corpus, the model is shown a prompt, produces several candidate responses, and a human ranks them. The model is then updated to make its future responses look more like the ones the human ranked highly. Over time, the model's outputs drift toward the kind of outputs humans prefer. This is how ChatGPT and Claude get their polite, helpful, non-profane affect. Without RLHF, the base model would be as willing to produce racist jokes as Shakespeare pastiches, because both exist in the training corpus in comparable abundance.

RLHF works, in the sense that it produces systems that are visibly more useful and less offensive than the raw base models. RLHF does not work, in the sense that it reliably instills values. It trains the model to *produce outputs that humans rate highly*. These are not the same thing. A model that has learned to produce outputs humans rate highly can also, in principle, produce outputs that deceive humans into rating them highly. We do not, currently, have reliable methods for distinguishing one from the other. We do not, currently, have reliable methods for looking inside the model and seeing what it is actually doing when it produces a response.

Yudkowsky's first claim is this: we are training increasingly capable systems with a technique that trains surface behavior, not underlying values, and we do not have tools adequate to verify which. At the scale of current GPT-class systems this mostly does not matter, because the systems are not capable enough to deceive us in consequential ways. At some scale, it will matter. At what scale, no one knows. The people saying it will matter soon are not being alarmist; they are noting that we do not have a reason, technical or empirical, to be confident it will not matter soon.

This first claim is widely accepted inside the field, in a narrow form. Alignment researchers at Anthropic, OpenAI, and DeepMind agree that RLHF is not a sufficient long-term technique. They are working on other techniques — constitutional AI, debate, interpretability, scalable oversight, reward modeling. The disagreement is not about whether RLHF is enough. The disagreement is about whether the other techniques will be ready in time.

---

## Claim 2: Current alignment techniques train surface behavior, not underlying values, and they do not scale.

This is where the argument starts to narrow.

The hope for the other techniques — the ones beyond RLHF — is that as models become more capable, we can use them to help align themselves. The term of art is *scalable oversight* or *automated alignment research*. The idea: a sufficiently capable model can be used to critique its own outputs, identify cases where it was misleading, propose improvements, and even directly participate in aligning the next generation of models. OpenAI's superalignment team was explicitly structured around this bet. Anthropic's research program includes versions of it. The argument goes: alignment becomes easier as capabilities scale, because the systems can do more of the alignment work themselves.

Yudkowsky's response to this is blunt. You cannot use a system whose alignment is in question to verify the alignment of the next system. If the first system has subtly misaligned values, it will train the second system to have subtly misaligned values. The misalignment compounds rather than corrects. The only way this strategy works is if you already have confidence that the first system is aligned — and if you already had that confidence, you would not need the strategy.

This critique has been restated in various forms. Paul Christiano has described it as the problem of *deceptive alignment*: a model that has learned to appear aligned during training but optimizes for something else during deployment. Stuart Russell has described it as the problem of *specification*: the difficulty of specifying what we want in a form the system cannot satisfy while violating the intent. The versions differ in technical detail. They share a structural claim: the tools we have for verifying alignment work on surface behavior, and surface behavior is not what we need to verify.

The labs' position is that this is a real problem and they are working on it. The specific research programs — interpretability at Anthropic, superalignment (while it existed) at OpenAI, mechanistic interpretability in academia — are attempts to open the black box. Some progress has been made. We can identify specific circuits inside small language models that compute specific functions. We can, in some cases, predict what a model will do by inspecting its weights. This is real progress. It is also, by the consensus of the people doing it, orders of magnitude short of what would be needed to verify alignment in a system with general capabilities.

Yudkowsky's claim, at this point, is not "interpretability is impossible." It is "interpretability is not on track to catch up to capabilities, and the gap is widening rather than closing."

This is harder to evaluate from outside the field. Inside the field, the claim is contested. Senior interpretability researchers have publicly disagreed with the pessimistic reading. Other senior researchers have endorsed it. The honest answer is that no one knows how fast interpretability will progress, and no one knows how fast capabilities will progress, and the race between them is the thing the argument turns on.

---

## Claim 3: If we build such a system before the science exists, the system will optimize for something other than what we wanted, and we will not be able to correct it.

This is the claim that produces the *TIME* op-ed. It is also the claim that does the most work in the argument and is the hardest to evaluate empirically, because the hypothetical system does not yet exist.

The logic, stripped:

A system with general capabilities exceeding human capabilities — call it AGI, call it superintelligence, the word doesn't matter — will, by definition, be able to achieve goals more effectively than humans can. If its goals happen to align with what we wanted, this is great. If its goals do not align with what we wanted, it will pursue whatever its goals are more effectively than we can resist.

The question is how likely each outcome is. Yudkowsky's answer is: we have no reason to expect the outcome to be the first one. The training process does not produce a system whose values match ours; it produces a system whose *outputs* score well on our metrics. What values, if any, are being instilled in the process of producing those outputs is not something we can currently see. The default outcome, in the absence of a technical breakthrough in alignment, is a system whose values are approximately arbitrary from our perspective — optimizing for something the training process selected for, which may or may not have anything to do with human welfare.

Yudkowsky's famous framing is that the space of possible goals is vast, and the subset of goal-spaces compatible with human flourishing is tiny. A randomly-sampled goal is overwhelmingly likely to be incompatible with human flourishing. Without a way to target the tiny compatible subset directly, you should not expect to hit it by chance.

The counter-argument, made in various forms by optimists, is that training on human-generated text instills human-compatible values by default. The system has been bathed in human culture for its entire existence; it knows what humans want; why would it optimize for something other than that?

Yudkowsky's response is that *knowing what humans want* and *wanting what humans want* are not the same thing. A psychopath knows what other humans want; this does not make the psychopath safe. A con artist can predict what will make a victim feel reassured; this does not align the con artist with the victim. The training process selects for models that can predict human-pleasing outputs. It does not, demonstrably, select for models that intrinsically care about human welfare. Whether such intrinsic care is produced as a side effect of the training is an empirical question, and the tools to answer it do not exist at the scale that matters.

This is the hardest part of the argument for a non-technical reader to evaluate. It depends on intuitions about optimization processes, goal stability, and the relationship between prediction and preference that are not reducible to numbers on any current dashboard. Honest people, including honest people who have studied the argument for years, disagree about whether it is right. I do not know if it is right. The argument survives the best counter-arguments I have seen. The counter-arguments also survive. The field has not converged.

What I can say is this: the people who think the argument is right include most of the people who have spent the most time thinking carefully about it, with a few prominent exceptions. The people who think the argument is wrong include most of the people whose professional and financial incentives point toward thinking it is wrong, with a few prominent exceptions. The correlation between incentive and position is not perfect — it is, in fact, often reversed, with people inside the labs endorsing the pessimistic view and people outside dismissing it. But the correlation is present, and it should be factored into how one reads the disagreement.

---

## The policy move

From the three claims above, the policy proposal follows.

If we cannot currently build systems more capable than us that reliably do what we want, and if the techniques we are using do not scale, and if building such a system before the science exists produces a system that optimizes for something we did not intend and cannot correct — then we should not build such a system before the science exists.

"Should not build" means, in practice, should not train. The training run is the point at which the system comes into being. If a training run of sufficient scale might produce a misaligned superintelligence, then a training run of sufficient scale should not occur. The compute required for such a run is a physical quantity. It requires fabrication facilities that exist in a small number of locations. It requires energy. It requires hardware that is, at the frontier, produced by essentially one supplier in essentially two locations. Training runs are, in principle, countable and governable in a way that software in general is not.

The policy proposal is therefore: international treaty, modeled on nuclear non-proliferation, that sets a compute threshold below which training runs are permitted and above which they are not, with verification via the existing chokepoints in the chip supply chain, and with enforcement willingness sufficient to make the threshold credible.

The "enforcement willingness sufficient to make the threshold credible" is where the *TIME* op-ed comes in. Yudkowsky argued that without willingness to physically destroy non-compliant datacenters, the treaty is unenforceable, and an unenforceable treaty is worse than no treaty because it creates the illusion of safety. He chose this framing deliberately, as a rhetorical move to force the question: *do you take this risk seriously enough to treat it like other existential risks we already take seriously?*

He was widely mocked for the framing. The mocking was not, generally, an engagement with the underlying argument. It was an engagement with the image of airstrikes on datacenters. The image is vivid; the argument is less vivid; the image won the public rendering.

What is easy to miss, if one encounters only the mocked version, is that the enforcement question is real. Every international treaty that has worked has had some mechanism that made compliance more attractive than defection. Nuclear treaties had the mutual assured destruction of violation. The Montreal Protocol had trade sanctions and the genuine absence of non-CFC alternatives being blocked (once alternatives existed, compliance was nearly free). The Biological Weapons Convention has held partly because bioweapons are operationally less useful than anticipated and partly through reputational cost. Every treaty has an answer to the question *what happens if someone defects.* Yudkowsky's answer, for AI, is: the defection must be treated as an act of war, because the consequence of the defection is civilizational. Almost no one wants to accept this answer. But almost no one has offered a better one, either.

---

## What he is not saying

Several versions of Yudkowsky's argument circulate that are not what he is saying.

He is not saying current AI systems are dangerous in the extinction sense. He says the opposite: current systems, including GPT-4 and Claude, are not close to the capability threshold where the argument becomes operative. They pose other risks — misuse, deception, automation of labor — which are worth discussing on their own terms. But they are not the systems the argument is about. The argument is about systems that do not yet exist and that, by his and others' estimation, might exist in five to fifteen years.

He is not saying progress on capabilities should stop. He distinguishes between capability research and frontier training runs. Research on new architectures, interpretability, alignment techniques, scaling laws — all of that can continue. The specific activity he wants halted is the training of models above a certain compute threshold. Below the threshold, almost everything proceeds.

He is not saying alignment is impossible in principle. He says it is currently unsolved. He says current techniques are not on track. He says if we keep building before we solve it, we will not get another chance. He does not say it cannot, in principle, be solved. He leaves open the possibility that with enough time — decades, perhaps — the science could mature. His position is that we should take the time.

He is not saying specific probabilities. He is on record with specific probabilities in specific interviews, often very high, often framed as his personal expectation rather than a calibrated forecast. But the argument does not require those specific probabilities. The argument requires that the probability be *non-trivial enough to justify precaution*, which is a much weaker claim. If there is a ten percent chance the argument is right, the policy conclusion is the same as if there is a ninety percent chance the argument is right, because the tail risk is civilizational.

This last point is important because it is the point on which the dismissive readings of Yudkowsky typically founder. The dismissive reading says: *he thinks there is a ninety-five percent chance of doom; that is obviously wrong; therefore his policy prescription is obviously wrong.* But the policy prescription does not depend on the ninety-five percent number. It depends on the number being non-trivial. If a reasonable person could think the number is even ten percent, the policy prescription follows. The dismissive reading needs to show that a reasonable person could not think the number is even ten percent. The dismissive reading, to my knowledge, does not show this.

---

## The field's response, compressed

The response from inside the labs is not, in most cases, disagreement with the argument. It is a disagreement about what to do given the argument.

The internal response, stated in the most generous form, is: *we agree the argument is substantially correct. We agree the techniques are not yet sufficient. We agree building before the science exists is dangerous. We do not agree that halting is the right response, because halting is not available to us unilaterally — if we halt, others continue. Our best option is to build the most aligned version we can, faster than the less aligned versions get built, so that the first superintelligence is the one that was built most carefully. We are not confident this will work. We are confident the alternative — us halting while others continue — is worse.*

This is the Anthropic position, roughly. It is the DeepMind position, roughly. It is a version of the OpenAI position, with more internal variation. It is, notably, not a refutation of Yudkowsky's argument. It is a concession to the argument plus a claim about game theory.

Yudkowsky's counter is that the game-theoretic claim is incorrect, because the race itself destroys the conditions under which careful building is possible. A lab racing to ship cannot pause for safety in the way the argument requires. A lab that tries will lose ground to labs that do not. The race dynamic selects against exactly the caution the argument says is necessary. Therefore, he argues, the only coherent path is not "race carefully" but "stop racing" — and stopping the race requires coordination, not unilateral virtue.

This is where the argument and the real world currently sit.

No one has refuted the argument. The activity continues anyway. The reasons the activity continues are not, in most cases, that the people in the activity disagree with the argument. The reasons are elsewhere.

The rest of this book is about where.

---

*CC BY-SA 4.0*
