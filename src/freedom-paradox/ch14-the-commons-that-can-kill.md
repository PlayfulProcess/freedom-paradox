# Chapter 14: The Commons That Can Kill

In 2009, the Nobel Committee in Economics did something unusual. It gave the prize to a political scientist.

Elinor Ostrom was not an economist in any conventional sense. She did not build mathematical models. She did not prove theorems about market equilibria or derive optimal taxation schedules from first principles. She went to places — Swiss alpine meadows, Japanese fishing villages, irrigation systems in Spain and the Philippines, forests in Nepal — and she watched what people actually did. She took notes. She came back and wrote about it.

What she found overturned one of the most influential metaphors in twentieth-century thought.

---

## The Tragedy That Wasn't

In 1968, the ecologist Garrett Hardin published an essay in *Science* called "The Tragedy of the Commons." The argument was elegant and devastating. Imagine a pasture shared by several herders. Each herder has an incentive to add one more cow to the pasture. The benefit of the additional cow accrues entirely to the individual herder. The cost — the marginal degradation of the shared grass — is distributed across all herders. The rational move, for each herder, is to keep adding cows. The result: the pasture is destroyed.

Hardin's conclusion was stark. Shared resources were doomed. The only solutions were privatization — divide the pasture into individually owned plots — or government regulation — have the state impose limits on grazing. There was no third option. The commons, left to human nature, would always be devoured.

The essay became one of the most cited papers in the history of environmental science. It shaped policy for decades. And it was, in important ways, wrong.

Ostrom proved it wrong not with theory but with evidence. She documented hundreds of communities around the world that had successfully managed shared resources for centuries. Swiss farmers had maintained alpine meadows since the thirteenth century through communal rules so sophisticated that they governed not just how many cows each family could graze but when, where, and under what weather conditions. Japanese fisheries operated under village cooperatives that allocated fishing rights, monitored catches, and sanctioned violators — without government intervention, without privatization, and without destroying the fish.

The commons could work. But not automatically. Ostrom identified eight design principles that distinguished the communities where shared resources survived from those where they collapsed. The principles were not laws. They were conditions — institutional features that, when present, made collective governance viable.

She called them design principles because they were not accidents. They were built. Communities that survived had, through trial and error over generations, constructed the institutional architecture that Hardin said was impossible.

---

## Eight Principles for a Shared World

The principles are worth stating precisely, because we are about to break them.

**First: clearly defined boundaries.** Successful commons define who has the right to use the resource and where the resource begins and ends. The Swiss meadow has a property line. The Japanese fishing cooperative has a membership roster. If you cannot say who is in the commons and what the commons contains, you cannot govern it.

**Second: congruence between rules and local conditions.** The rules that govern the Swiss meadow reflect the ecology of the Swiss meadow — its altitude, its soil, its rainfall. The rules that govern the Japanese fishery reflect the migration patterns of the local fish. Governance works when rules are fitted to the thing being governed, not imposed from an abstract template.

**Third: collective-choice arrangements.** The people affected by the rules get to participate in making the rules. Not a distant legislature. Not a foreign regulator. The farmers who graze the meadow vote on how many cows the meadow can sustain. This is not democracy as ideology. It is feedback — the people with the most information about the resource make the decisions about the resource.

**Fourth: monitoring.** Someone watches. Not a distant bureaucracy, but monitors accountable to the community — often the community members themselves. The key is not surveillance but transparency: can the community see what is happening to the resource?

**Fifth: graduated sanctions.** First offense gets a warning. Second offense gets a fine. Third offense gets exclusion. The punishment escalates, giving violators a chance to correct behavior before the penalty becomes severe. This works because it preserves the community — a single catastrophic punishment for a first-time offender destroys the cooperative relationship that makes the commons function.

**Sixth: conflict-resolution mechanisms.** When disputes arise — and they always arise — there must be an accessible, low-cost way to resolve them. Village councils. Elders. Local courts. What matters is that resolution is available without destroying the community in the process.

**Seventh: minimal recognition of rights to organize.** The government — or whatever external authority exists — recognizes the community's right to govern itself. It does not override the fishing cooperative's rules with national legislation. It does not replace the farmers' council with a federal agency. It allows the commons to be governed by the people who use it.

**Eighth: nested enterprises.** For large-scale commons, governance is organized in layers. Local rules nest within regional frameworks, which nest within national policies. Each layer handles the problems appropriate to its scale.

These eight principles were not idealistic. They were descriptive. Ostrom found them by studying what worked. She was an empiricist in a field of theorists, and her empiricism won her the Nobel Prize.

---

## The Test

For forty years, Ostrom's principles have been applied to fisheries, forests, irrigation systems, grazing lands, and groundwater basins. They have been adapted for digital resources — open-source software, Wikipedia, Creative Commons. The Linux kernel, governed by a community of thousands of contributors under Linus Torvalds's stewardship, is in some ways the greatest commons success story in history: a shared resource that has been maintained, improved, and governed collectively for more than three decades. It runs the servers, phones, and infrastructure of the modern world. The commons, when designed well, can scale to planetary dimensions.

The question this chapter must ask is whether the commons can scale to AI.

The instinct is to say yes. After all, AI models share important features with successful digital commons. Open-source models like Meta's Llama and Alibaba's Qwen are distributed freely. Anyone can download them, modify them, contribute improvements. The code is visible. The community is global. If Linux proved that Ostrom's principles could govern software, perhaps they can govern AI.

Let us test each principle against the reality of AI in 2026. The exercise will be systematic, and the results will be uncomfortable.

---

## Principle by Principle

**Boundaries.** In a successful commons, you can define who is in and what the resource contains. The Swiss meadow has a fence. The fishing cooperative has a membership list. Even the Linux kernel has a defined set of maintainers with commit access and a clear boundary around what constitutes the kernel versus user-space software.

An AI model released under an open license has no boundaries in any meaningful sense. Once Meta publishes the weights of Llama, the "community" of users is anyone on earth with sufficient hardware. There is no membership roster. There is no fence. The model can be downloaded in Palo Alto or Peshawar, used by a cancer researcher or a weapons designer, fine-tuned for medical diagnosis or for generating synthetic child exploitation material. The boundary of the commons is the boundary of the internet itself.

This is not a minor deviation from Ostrom's framework. Boundaries are the first principle because they are the precondition for every other principle. Without knowing who is in the commons, you cannot organize collective choice (Principle 3), conduct monitoring (Principle 4), or impose sanctions (Principle 5). The entire governance architecture rests on knowing who you are governing.

**Congruence.** Rules must match local conditions. Swiss farmers know their soil. Japanese fishers know their currents.

AI models do not have local conditions. The same model operates in every domain simultaneously — medicine, law, creative writing, cybersecurity, biological research. A rule that makes sense for medical AI (rigorous validation, clinical trials) is absurd for creative writing AI. A rule that makes sense for creative writing (broad freedom of expression) is potentially catastrophic for biological research (where the same broad freedom enables pathogen design). There are no "local conditions" to match rules to because the resource operates everywhere at once.

**Collective choice.** Those affected by the rules should participate in making them.

Who is affected by the rules governing an AI model? The developer who trained it. The company that released it. The researchers who fine-tune it. The users who interact with it. The people depicted in its training data without their knowledge. The workers in the Global South who labeled that data. The citizens whose elections may be disrupted by synthetic media generated from it. The future generations who will inherit whatever epistemic environment these models create.

The "community" affected by a frontier AI model is, in practice, everyone alive. Ostrom's principle of collective choice works because the community is defined. When the community is the entire human population, collective choice becomes a euphemism for global politics — and global politics, as anyone who has watched climate negotiations can attest, is not a governance mechanism that inspires confidence.

**Monitoring.** Someone must watch what happens to the resource.

When Claude or GPT responds to a query through an API, the provider can monitor the interaction. Usage policies can be enforced. Patterns of misuse can be detected. This is not commons governance — it is corporate governance — but it functions as monitoring.

When a model's weights are released openly, monitoring becomes impossible in a meaningful sense. The model runs locally on the user's hardware. There is no phone home, no telemetry, no audit trail. A user who strips safety training from an open model and fine-tunes it for generating phishing emails or synthesizing instructions for chemical weapons does so in perfect privacy. No fishing inspector walks the dock. The ocean is dark.

**Graduated sanctions.** First a warning, then a fine, then exclusion.

A model released under the Apache 2.0 license cannot be recalled. There is no mechanism for a first warning. By the time harmful use is detected — if it is detected at all — the model has proliferated across thousands of servers, been incorporated into downstream applications, been fine-tuned into specialized tools. Sanctioning the original developer does nothing about the copies. Sanctioning a downstream user requires first identifying them, which requires the monitoring that does not exist.

The time horizon is the problem. Ostrom's graduated sanctions work because the commons exists over time. The fisher who is warned today can be fined tomorrow and excluded next month. The resource — the fishery — is still there, being managed. An AI model's harmful deployment is often a one-shot event. The deepfake that disrupts an election. The biological agent designed from an open model. The autonomous weapon deployed in a conflict. These are not ongoing activities that can be gradually discouraged. They are irreversible events.

**Conflict resolution.** Accessible, low-cost dispute resolution.

The three major AI governance regimes — the European Union's AI Act, the United States' patchwork of executive orders and state legislation, and China's state-directed regulatory framework — reflect fundamentally incompatible visions of what AI governance should accomplish. The EU prioritizes individual rights. The US prioritizes innovation. China prioritizes state control. There is no mediator. There are no village elders. The AI Safety Summits — Bletchley Park in 2023, Seoul in 2024, Paris in 2025 — have produced declarations and communiques but no binding agreements and no enforcement mechanisms.

**Rights to organize.** External authorities recognize the community's self-governance.

Open-source software foundations — the Apache Foundation, the Linux Foundation, the Python Software Foundation — represent genuine commons self-governance that governments have recognized and respected. But these foundations govern code, not capabilities. The governance question for AI is whether a community can self-govern a technology with catastrophic risk potential.

Governments are answering that question with legislation, not recognition. The EU AI Act does not recognize community self-governance for high-risk AI systems. It imposes requirements from above. This is not because governments are hostile to commons governance. It is because the stakes of AI governance — biosecurity, autonomous weapons, mass surveillance, epistemic integrity — are stakes that no government will delegate to a voluntary community.

**Nested enterprises.** Governance organized in layers, local to global.

This is perhaps the most painful failure. Effective AI governance would require nested institutions: local AI safety boards, national regulatory agencies, regional frameworks (like the EU AI Act), and a binding international treaty with monitoring and enforcement power — an IAEA for AI, as Sam Altman and others have proposed. [VERIFY: exact Altman quote on IAEA for AI]

No such architecture exists. National regulations conflict. International coordination is aspirational. The fragmentation is not accidental — it reflects the genuine difficulty of governing a technology that respects no borders, serves every purpose, and operates at the speed of software distribution.

---

## The Paradox of the Non-Rivalrous Harm

Here is where the analysis must go deeper.

Ostrom's framework was designed for common pool resources — goods that are rivalrous and non-excludable. Rivalrous means one person's use diminishes what is available to others. One fish caught is one fish gone. One tree felled reduces the forest. The whole point of commons governance is to prevent the shared resource from being consumed to exhaustion.

AI models are not rivalrous. Downloading Llama does not diminish Meta's copy. A thousand researchers fine-tuning Qwen for a thousand different purposes do not reduce the model's availability to the thousand-and-first researcher. The model is non-rivalrous — and this is precisely why the code commons (Linux, Apache) has worked so well. Non-rivalry means there is nothing to deplete.

But the harms that AI enables are rivalrous. They consume shared resources that are depletable, often irreversibly.

Social trust is a commons. Every convincing deepfake that circulates — every fabricated video of a politician, every synthetic audio of a CEO authorizing a fraudulent transaction, every generated image that is indistinguishable from a photograph — erodes the shared resource of epistemic trust. When no one can be certain whether any video is real, the baseline assumption shifts from trust to suspicion. This is a tragedy of the commons in Hardin's exact sense: each producer of synthetic media captures individual benefit (attention, influence, fraud proceeds) while distributing the cost (erosion of collective trust) across everyone. [VERIFY: deepfake growth rate — reports suggest 900% annual increase]

Privacy is a commons. Mass surveillance powered by AI facial recognition, behavioral prediction, and data aggregation degrades the shared expectation that public spaces are not spaces of total observation. One actor's deployment of surveillance infrastructure diminishes everyone's privacy, even those who are not directly surveilled, because the *possibility* of surveillance alters behavior. The chilling effect is itself a form of commons depletion.

Security is a commons. The proliferation of autonomous weapons creates the classic dynamics that Ostrom's framework was designed to prevent — an arms race where each actor's rational self-interest (more weapons, better weapons) degrades the shared resource of collective security. Every autonomous weapon deployed makes every other actor less safe.

Biosafety is a commons. This is the sharpest case. Open biological AI models — models capable of protein design, pathogen engineering, genetic modification — create a situation where one bad actor's use can cause catastrophic, irreversible harm. Researchers have demonstrated that AI protein-design tools can redesign toxic proteins in ways that evade DNA synthesis screening. The shared resource of biosafety, painstakingly built over decades of international agreements and voluntary industry practices, can be depleted by a single act.

The paradox, then, is this: the AI model itself is not a traditional commons problem. It is a non-rivalrous good, like knowledge or code. But the *harms* that flow from it are classic commons problems — rivalrous, depletable, and subject to exactly the tragedy that Hardin described and Ostrom tried to solve.

Ostrom's framework governs the resource. It was not designed to govern the externalities of a resource that is itself free.

---

## The Nuclear Mirror

When AI leaders reach for an analogy, they often reach for nuclear weapons.

The comparison has surface appeal. Both technologies are dual-use — capable of tremendous benefit and catastrophic harm. Both involve a small number of actors with the most advanced capabilities and a larger number who want access. Both raise the question of whether international cooperation can prevent the worst outcomes.

Sam Altman has proposed an international regulatory body modeled on the International Atomic Energy Agency. Bill Gates has described AI and nuclear technology as rare cases where a technology is simultaneously promising and dangerous enough to require governance at the civilizational level. The analogy has become so pervasive that *Nature Reviews Physics* published a paper in 2025 asking why it was so popular.

The answer to that question also reveals why the analogy is misleading.

Nuclear nonproliferation works — imperfectly, but meaningfully — because nuclear weapons are hard to build. Enriching uranium requires centrifuges, which require precision engineering, which requires supply chains that can be monitored. Producing plutonium requires reactors, which are large, hot, and visible to satellites. The entire architecture of the Nuclear Non-Proliferation Treaty rests on the fact that the *physical requirements* of nuclear weapons development create chokepoints where governance can be applied. You cannot enrich uranium in secret for long because the infrastructure is detectable.

AI has no such chokepoints. Training a model requires GPUs and data. GPUs are commercially available — NVIDIA ships them to data centers worldwide. Data is the internet itself. The "enrichment" process — training — produces no detectable physical signature. A frontier model can be trained in a data center that looks, from the outside, like every other data center on the block.

The nuclear analogy also rests on a distinction that AI does not have: the separation between civilian and military applications. A nuclear reactor generates electricity. A nuclear weapon destroys cities. The technology is the same at a fundamental level, but the artifacts are different, and the difference is detectable and governable. You can inspect a facility and determine whether it is enriching uranium to five percent (reactor fuel) or ninety percent (weapons grade).

AI has no equivalent gradient. The model that helps a researcher design a cancer drug is architecturally identical to the model that could help a different user design a pathogen. There is no "enrichment percentage" that separates peaceful AI from dangerous AI. The capability is the same. The intent is different. And intent is invisible to inspection.

Perhaps most critically: nuclear material cannot be copied. If a state possesses twenty kilograms of weapons-grade uranium, that is twenty kilograms. It cannot be duplicated, emailed, or posted to a GitHub repository. AI model weights can be. Once released, they propagate at the speed of file transfer. The NPT's verification regime works because there is a finite, physical thing to verify. Open AI models are infinite, digital, and beyond recall.

Georgetown's Center for Security and Emerging Technology published a direct challenge to the analogy in 2024, arguing that AI differs so fundamentally from nuclear technology that basing AI governance on the nuclear framework risks creating false confidence in our ability to control proliferation. The nuclear model suggests that a treaty, an inspectorate, and a verification regime can manage the risk. For AI, there may be nothing to inspect and no way to verify.

---

## What the Code Commons Cannot Teach Us

There is a more hopeful analogy available, and it is closer to home: the open-source software commons.

The Linux kernel has been governed collectively for over thirty years. The Apache web server, the PostgreSQL database, the Python programming language — these are genuine commons, maintained by communities of contributors, governed by foundations with transparent processes, and used by billions without depleting the resource. Ostrom, had she studied open-source software, would have recognized her principles at work. The communities have defined membership (Principle 1). Rules match the technical domain (Principle 2). Contributors participate in decision-making (Principle 3). Code review serves as monitoring (Principle 4). Bad actors face graduated consequences — rejected patches, revoked commit access, community exclusion (Principle 5).

The code commons works. It is one of the great collective achievements of the late twentieth and early twenty-first centuries. And it may have nothing to teach us about governing AI.

The reason is revertibility. A malicious patch submitted to the Linux kernel can be caught in code review — and if it slips through, it can be reverted. The damage is bounded. A security vulnerability discovered in Apache can be patched. The fix propagates. The commons recovers.

AI capabilities cannot be reverted. A model that has been fine-tuned to generate synthetic biological agents does not become safe because someone issues a patch. The knowledge embedded in model weights is not a line of code that can be commented out. The capability exists, distributed across millions of floating-point parameters in a way that cannot be surgically removed.

This is the fundamental disanalogy. The code commons assumes that errors are correctable. The AI commons must contend with the possibility that errors are permanent.

---

## The Question the Commons Cannot Answer

Elinor Ostrom gave us the most sophisticated, empirically grounded framework for collective governance that exists. She proved that communities could manage shared resources without either the heavy hand of the state or the atomization of private property. She demonstrated, across cultures and centuries, that human beings were capable of cooperation more nuanced than Hardin imagined.

Her framework works for fisheries. It works for forests and meadows and irrigation canals. It works for code — the Linux kernel, the Apache web server, the vast ecosystem of open-source software that undergirds the digital world. It works, in its way, for knowledge — Wikipedia is a commons governed by principles Ostrom would recognize.

It may not work for AI.

Not because Ostrom was wrong. She was profoundly right about the conditions under which collective governance succeeds. The problem is that AI violates those conditions in nearly every particular. Its boundaries are undefined. Its "local conditions" are global. Its community is everyone. It cannot be effectively monitored once released. Sanctions cannot be graduated against a non-recallable artifact. Conflict-resolution mechanisms do not exist at the international scale required. Governments are not recognizing commons self-governance; they are imposing regulation from above. And the nested institutional architecture that successful large-scale commons require has not been built.

The nuclear analogy offers no rescue. Nuclear governance works because the technology is hard and physical. AI governance must contend with a technology that is easy and digital. The NPT verifies enrichment facilities. There is no facility to verify when the dangerous artifact is a file.

And the code commons, for all its beauty, governs a resource whose harms are bounded and reversible. A buggy kernel crashes a server. A misused AI model can crash an election, a biosecurity regime, or the shared epistemic foundation on which democratic societies depend.

This is the bind. The best framework we have for governing shared resources — developed over decades, validated across cultures, honored with the Nobel Prize — was designed for resources that are bounded, local, monitorable, and recoverable. AI is none of these things.

The commons framework asks: how do we prevent overexploitation of a shared resource? The AI question is different. It asks: how do we govern a resource that cannot be depleted but whose use can cause irreversible harm? How do we impose boundaries on something that has no edges? How do we monitor something that runs in the dark? How do we sanction something that cannot be recalled?

Ostrom showed us that the tragedy of the commons is not inevitable. The question now is whether there are tragedies beyond the commons — harms that no governance framework, however elegant, can prevent once the resource is free.

Part V of this book is called The Question because there may not be an answer. But the question must be stated precisely before we can begin to look for one. It is this: can we have commons governance for a technology that, once released into the commons, cannot be governed at all?

The Swiss farmers managed their meadow for seven hundred years. The Japanese fishers sustained their waters for generations. They did it by building institutions that matched the nature of the resource.

The nature of this resource is different. And we are only beginning to understand how different.
