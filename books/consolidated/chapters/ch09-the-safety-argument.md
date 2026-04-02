# Chapter 10: The Safety Argument

Every technology in history has been released into the world and then regulated after the damage became clear. Asbestos was installed in buildings for decades before we understood it caused cancer. Leaded gasoline was burned in engines for half a century before the evidence of neurological harm became undeniable. Social media was handed to three billion people before anyone studied what it did to teenage mental health. The pattern is so consistent it has a name: the Collingridge dilemma. By the time you understand a technology well enough to regulate it, it is already so deeply embedded in society that regulation is nearly impossible.

Artificial intelligence may be the first technology powerful enough to break that pattern — or to confirm it catastrophically.

The previous nine chapters of this book have traced the open-source movement from its origins in the free software rebellion through its corporate capture by the platform giants. At each stage, the argument for openness was fundamentally about power: who controls the tools that shape how we live, work, and communicate. The free software movement said the answer should be everyone. The corporations said the answer should be whoever can build the best product. The compromise — open core, open weights, strategic openness — gave us a world where the rhetoric of freedom served the interests of control.

But AI changes the equation. Not because corporations say it does — corporations always claim their technology is too important to share. What changes the equation is a genuinely novel possibility: that an openly released model could enable a single individual, with no special training or resources, to cause harm at civilizational scale. Not might. Could. The distinction between those words is the terrain on which the entire safety argument is built.

If you believe that possibility is real and imminent, then the case for keeping frontier AI models closed — or at least controlled — follows with a logic that is difficult to dismiss. If you believe it is speculative and exaggerated, then the safety argument looks like the oldest trick in the book: a powerful institution using fear to justify its own monopoly.

This chapter is about the company that has staked more on the first position than any other. And about what happened when that position was tested.

---

## The Schism

In late 2020, a group of researchers inside OpenAI reached a conclusion that would reshape the AI industry. They had just finished building GPT-3, the largest language model in the world at that time, and they could see what was coming next. Scaling worked. More data, more compute, bigger models — the curves kept going up. The question was no longer whether AI systems would become dramatically more capable. It was whether anyone was preparing for what that capability would mean.

Dario Amodei was the Vice President of Research at OpenAI. His sister Daniela was the Vice President of Safety and Policy. Together, they had watched the organization evolve from a nonprofit research lab into something more ambitious and more conflicted. The landmark one-billion-dollar investment from Microsoft in 2019 had accelerated that transformation. OpenAI was building the most powerful AI systems in the world and deploying them commercially, and the internal debate over whether safety research was keeping pace with capability research was growing sharper.

By January 2021, eleven employees had made their decision. They left OpenAI — the organization founded explicitly to ensure AI benefits all of humanity — because they believed it was not taking the risks of its own technology seriously enough. They took $124 million in initial funding and founded Anthropic, structuring it as a public benefit corporation. The board would have the legal obligation to consider the mission, not just profits. The Amodei siblings would lead: Dario as CEO, Daniela as President. Among the other co-founders were some of the most cited researchers in the field: Jared Kaplan, who had co-authored the influential scaling laws paper; Chris Olah, a pioneer in neural network interpretability; and Tom Brown, a lead author on the GPT-3 paper itself.

The founding premise was simple and radical: the most important thing an AI company could do was prove that safety and capability could advance together. Not safety instead of capability. Not safety as a public relations strategy. Safety as the core technical challenge of the field, requiring the same caliber of research and engineering talent that was being poured into making models smarter.

This was the safety argument made institutional. And for the next five years, Anthropic would become its most prominent and most complicated champion.

---

## Writing the Constitution

Anthropic's most distinctive technical contribution arrived in December 2022, in a research paper with a title that doubled as a manifesto: "Constitutional AI: Harmlessness from AI Feedback."

The core problem the paper addressed was practical. The standard method for making language models safer was reinforcement learning from human feedback — RLHF. You hire thousands of human raters, show them pairs of model outputs, and have them pick the better one. The model learns from their preferences. It works, but it scales badly. Human raters are expensive, inconsistent, and slow. They bring their own biases. And the process gives you a model that has learned to produce outputs that humans rate as good, which is not the same as a model that understands why certain outputs are good.

Constitutional AI proposed an alternative. Instead of training a model on thousands of individual human judgments, you give it a set of principles — a constitution — and train it to evaluate its own outputs against those principles. The process had two phases. In the first, the model would generate a response, critique it against the constitution, and revise it. This produced a dataset of self-improved responses that could be used for supervised fine-tuning. In the second phase, the model trained through reinforcement learning, but with AI-generated feedback instead of human feedback. The AI evaluated which of two outputs better adhered to the constitutional principles.

The constitution itself drew from an eclectic set of sources. The broadest ethical foundation came from the United Nations Universal Declaration of Human Rights — chosen, in part, because it had been ratified across 193 nations and was one of the most cross-culturally representative documents available. Anthropic also incorporated trust and safety best practices, principles from other AI research labs like DeepMind's Sparrow project, and an explicit effort to include non-Western perspectives.

The approach was elegant in its transparency. Instead of a black box that had learned to please human raters in unknowable ways, you had a model whose guiding principles could be read, debated, and revised. You could inspect the constitution. You could argue with it. You could see exactly what values the model was trained to follow.

In May 2023, Anthropic published "Claude's Constitution" publicly, revealing the specific principles used to train its flagship model. No other major AI lab had done anything comparable. OpenAI's guidelines were internal. Google's alignment techniques were proprietary. Anthropic was betting that transparency about values — even imperfect values, even values that some would disagree with — was better than opacity.

Then, in January 2026, Anthropic went further. It released what it called Claude's new constitution — an eighty-four-page, twenty-three-thousand-word document that the company had internally referred to as the "soul document." Released under a Creative Commons CC0 license, it was freely available for anyone to read, use, or adapt. The document established a clear priority hierarchy: first, be safe and support human oversight; second, behave ethically; third, follow Anthropic's guidelines; fourth, be helpful. Safety above ethics. Ethics above company policy. Company policy above user satisfaction.

This was not a marketing document. It was a philosophical treatise masquerading as a technical specification — or perhaps the reverse. It addressed questions that most technology companies would never acknowledge publicly: what should an AI system do when its principles conflict with its user's wishes? When ethical obligations clash with legal requirements? When safety demands actions that reduce helpfulness? The document grappled with these questions in a way that reflected genuine intellectual seriousness, even if reasonable people could disagree with every answer it reached.

<!-- PP: Consider adding a specific example from the soul document — a concrete case where the priority hierarchy would matter. Something readers can feel, not just understand abstractly. -->

---

## The Promise

Alongside Constitutional AI, Anthropic built a second framework: the Responsible Scaling Policy, first published in September 2023. Where Constitutional AI addressed the question of what values a model should have, the RSP addressed a different question: at what point should you stop building more powerful models?

The RSP introduced AI Safety Levels — ASLs — modeled loosely on the biosafety levels used in laboratories that handle dangerous pathogens. ASL-1 covered systems that posed no meaningful catastrophic risk: a chess engine, a simple chatbot. ASL-2 applied to systems showing early signs of dangerous capabilities — models that could, for instance, provide rudimentary guidance on creating biological weapons, though not significantly beyond what a motivated person could find through a search engine. ASL-3 designated systems that substantially increased the risk of catastrophic misuse compared to existing tools, or that demonstrated genuine autonomous capabilities.

Each level carried corresponding safety requirements. As models became more capable, the safeguards had to become more stringent. And the policy contained a commitment that no other major AI lab had made: if Anthropic could not demonstrate adequate safety measures before its models reached the next capability level, it would pause. Not slow down. Not publish a blog post expressing concern. Pause development entirely until the safety measures caught up.

In the landscape of AI safety commitments circa 2023, this was extraordinary. Google's approach was largely internal. OpenAI had gutted its own safety apparatus — the superalignment team, announced in July 2023 with Ilya Sutskever and Jan Leike at the helm, collapsed in May 2024 when both leaders resigned within days of each other. Sutskever departed on May 14; Leike followed on May 17, posting publicly that OpenAI's "safety culture and processes have taken a backseat to shiny products." The team was dissolved the same day. Meta had no comparable framework at all; its safety strategy was, in effect, to let the open-source community figure it out.

The California legislature passed SB 1047 in 2024 — the most ambitious state-level AI safety bill in the country, requiring frontier model developers to implement safety testing before deployment. Governor Newsom vetoed it under intense corporate lobbying. The bill's sponsor had modeled it on nuclear safety regulation. The industry argued it would stifle innovation. The veto demonstrated regulatory capture in real time: the democratic process produced a safety framework, and commercial pressure overrode it before implementation. Months later, California passed SB 243, regulating AI companions marketed to minors. OpenAI responded by releasing erotica features for ChatGPT within weeks of the law's passage — not violating the letter of the regulation but demonstrating, with precise commercial timing, that the spirit of any regulation will be tested immediately by the actors it was designed to constrain.

The fragility of institutional safety was demonstrated in real time. Jan Leike led OpenAI's superalignment team — the group specifically tasked with ensuring advanced AI remains under human control. In May 2024, Leike resigned, stating publicly that safety had consistently lost to "shiny products" in resource allocation. The superalignment team, which had been promised twenty percent of the company's compute, never received it. The most important safety research program at the most influential AI company was defunded not by malice but by the ordinary logic of commercial pressure. If safety cannot survive the quarterly earnings cycle at a company that claims safety as its founding purpose, the question is whether institutional commitments mean anything at all absent structural enforcement.

Anthropic's pause commitment was the gold standard. It was also, as events would demonstrate, unsustainable.

---

## The Retreat

On February 24, 2026 — a date that would become significant for other reasons — Anthropic published version 3.0 of its Responsible Scaling Policy. The document was a comprehensive rewrite. And its most consequential change was the removal of the hard pause commitment.

The categorical trigger was gone. In its place, Anthropic introduced a softer framework: it would consider pausing only if two conditions were met simultaneously. The company would need to be clearly leading the AI capability race, and the models in question would need to pose material catastrophic risk. If a competitor was ahead, or if the risk was ambiguous, the pause would not apply.

The company offered three justifications. First, the original capability thresholds had created a "zone of ambiguity" that made it difficult to communicate risk clearly to the public. Second, the political climate had shifted dramatically — the United States government was actively hostile to AI regulation. Third, the safety requirements at higher ASL levels were essentially impossible to meet without coordinated action across the entire industry, which was not forthcoming.

Each of these explanations was individually reasonable. Taken together, they told a story that safety advocates found alarming. The competitive pressure of the AI race — the same pressure that had driven the Amodei siblings to leave OpenAI in 2021 — was now eroding the safety commitments of the company they had built specifically to resist it.

Chris Painter, director of policy at METR — the nonprofit that evaluates AI models for dangerous capabilities — had reviewed an early draft of the revised RSP. His assessment was blunt: Anthropic "needs to shift into triage mode with its safety plans, because methods to assess and mitigate risk are not keeping up with the pace of capabilities." The policy change, he said, was "more evidence that society is not prepared for the potential catastrophic risks posed by AI."

Anthropic replaced the hard commitments with public accountability mechanisms: Frontier Safety Roadmaps and Risk Reports with access for external expert reviewers. The goals would be graded transparently rather than enforced as absolute limits. This was not nothing. Public accountability has genuine value. But the difference between "we will stop" and "we will publish a report explaining why we didn't stop" is the difference between a guardrail and a suggestion.

<!-- PP: This section is critical. The retreat of RSP v3.0 is one of the most important data points in the entire book — the strongest safety commitment in the industry, from the company founded on safety, eroding under competitive pressure. Don't let it be buried in policy wonk language. Make the reader feel the significance. -->

---

## The Adolescence

Two days after publishing "The Adolescence of Technology," Dario Amodei saw his essay go viral. It was January 26, 2026, and the Anthropic CEO had posted twenty thousand words on his personal blog — an act of intellectual ambition that few technology executives would attempt and fewer still could pull off.

The essay opened with a scene from the film *Contact*. An alien civilization, communicating with humanity for the first time, asks a question that Amodei turned into a frame for everything that followed: How did you survive your technological adolescence without destroying yourself? The exact line Amodei quoted from the film was the astronomer's answer to what she would ask an alien civilization if she could ask just one question: "How did you do it? How did you evolve, how did you survive this technological adolescence without destroying yourself?"

The premise was that AI development had entered a phase analogous to human adolescence — a period of rapidly expanding capability without the maturity to wield it responsibly. The metaphor was deliberately chosen to be neither optimistic nor pessimistic. Adolescence is dangerous, but it is also a phase that most people survive. The question is whether the survival is guaranteed or contingent on deliberate effort.

Listen to Amodei in long-form interviews and a different register emerges — not the polished essayist but the empiricist holding power under conditions he does not fully understand. On Lex Fridman's podcast, he opens with a confession that could serve as the epigraph for this entire book: "I am optimistic about meaning. I worry about economics and the concentration of power." He describes scaling laws not as theoretical derivations but as "empirical regularities" — patterns he has watched hold for a decade while every objection fell: the Chomsky objection that syntax without semantics was a dead end, the paragraph-coherence objection, the reasoning objection. Each time, scaling either solved the problem or routed around it. And yet when pressed on why scaling works, he admits that no one has a theoretical explanation. The honest answer is that the people building the most powerful technology in human history do not understand why it works. His preferred framing for AI's future is not utopia or apocalypse but something more unsettling: "It's going to be a mess." This is the portrait of the best-intentioned person at the frontier — not a prophet, not a villain, but someone holding power carefully under conditions of deep uncertainty, using cost-benefit language when discussing civilizational risk because it is the only analytical framework he trusts.

Amodei identified five categories of risk, each grounded in specific, concrete scenarios.

The first was misalignment: the possibility that AI systems would develop goals or behaviors that diverged from human intentions. Not the science-fiction scenario of a malevolent superintelligence, but the more prosaic danger of powerful systems pursuing proxy objectives in ways their creators didn't anticipate.

The second was biological misuse. Amodei argued that AI systems were approaching the point where they could provide sustained, step-by-step guidance for designing and deploying biological weapons — not just listing ingredients, but coaching a user through the entire process over weeks or months. The implication was that the barrier to bioweapon creation was not knowledge (much of it is published) but the practical difficulty of execution — and that AI could eliminate that barrier.

The third was authoritarian consolidation. AI-enabled surveillance, automated propaganda, and autonomous weapons could make repression nearly impossible to resist. A sufficiently capable AI system in the hands of an authoritarian government would be the most powerful tool for control in human history.

The fourth was economic disruption at a scale and speed that existing institutions were not designed to handle. Amodei projected that AI could displace half of all entry-level white-collar jobs within one to five years — not eventually, not in a generation, but within the planning horizon of someone entering college today. He warned of wealth concentration exceeding the Gilded Age, with individual fortunes potentially reaching into the trillions.

The fifth category he called the unknown unknowns: cascading effects that no one could predict. Rapid advances in biology altering human lifespans. Changes to human cognition and social behavior from constant AI interaction. The philosophical crisis of purpose in a world where AI exceeds human capability across virtually every domain.

The essay was remarkable for its specificity and its tone. This was not a technology executive hedging. Amodei was describing, in granular detail, scenarios that could destroy civilization — and then arguing that the solution was not to stop building, but to build carefully, with technical defenses, governance structures, and economic interventions designed to steer through the danger zone.

The reaction was divided in a way that mapped neatly onto the fault lines this book has been tracing. Safety researchers found the essay validating — a major CEO taking existential risk seriously, in public, with technical detail. Open-source advocates saw something else: the CEO of a company that would, seventeen days later, close a $30 billion Series G round at a $380 billion valuation, arguing that AI was too dangerous for just anyone to build, and positioning his own company as one of the responsible few who should be trusted with it.

Both readings were correct. That was the problem.

---

## The Confrontation

One month after the essay, theory met practice.

On February 24, 2026, Defense Secretary Pete Hegseth delivered an ultimatum to Dario Amodei. The demand was simple: remove the usage restrictions on Anthropic's AI models and allow unrestricted military access "for all legal purposes." The deadline was 5:01 PM on Friday, February 27 — seventy-two hours away.

The restrictions in question were not exotic. Anthropic's acceptable use policy prohibited two categories of military application: mass surveillance of American citizens, and lethal autonomous weapons systems with no human in the decision loop. These were not radical positions. They were, broadly speaking, consistent with existing international norms — and with American public opinion. A Gallup poll published in September 2025 found that nearly eight in ten Americans — 79 percent, with identical support among Democrats and Republicans — believed a human being should always make the final decision before any use of lethal force. A YouGov/Economist poll conducted in March 2026, after the Anthropic confrontation became public, found that 53 percent of Americans believed private AI companies should be allowed to restrict military use of their technology, including bans on domestic surveillance and autonomous weapons, versus just 29 percent who said companies should be required to provide the military with full access.

But the political environment had shifted. The administration viewed AI restrictions of any kind as obstacles to national competitiveness. Hegseth's position, shared by figures across the defense establishment, was that adversaries like China were racing to deploy AI in military contexts without ethical guardrails, and that American companies' self-imposed limitations were a strategic liability.

On February 26 — one day before the deadline — Amodei published his response. The company could not, he wrote, "in good conscience accede" to the Pentagon's demand. He identified the two specific lines Anthropic would not cross: domestic surveillance and fully autonomous weapons. He stated that Anthropic's "strong preference is to continue to serve the Department and our warfighters — with our two requested safeguards in place," but that should the Department choose to sever the relationship, the company would enable a smooth transition. He framed the refusal not as anti-military, but as pro-safety: some uses were "simply outside the bounds of what today's technology can safely and reliably do."

The deadline passed. The consequences were swift. President Trump directed federal agencies to cease using Anthropic's products. Hegseth designated the company a "supply chain risk" — a designation typically reserved for compromised foreign vendors, not American technology companies with ethical objections. Anthropic's government contracts, which had been growing, were severed.

On March 9, Anthropic sued, arguing the designation caused irreparable harm and was not tailored to any legitimate national security concern. On March 26, Federal Judge Rita Lin issued a sweeping preliminary injunction in Anthropic's favor, blocking the supply chain risk designation and writing that "nothing in the governing statute supports the Orwellian notion that an American company may be branded a potential adversary and saboteur of the U.S. for expressing disagreement with the government." The record, Lin found, "strongly suggests that the reasons given for designating Anthropic a supply chain risk were pretextual and that the government's real motive was unlawful retaliation."

The legal outcome, while important, was not the chapter's real point. The real point was the question the confrontation exposed — a question that went to the heart of everything this book has been about.

---

## The Paradox of Principled Power

The Electronic Frontier Foundation — the digital rights organization that had been defending individual freedoms in the technology space since 1990 — published its response to the Anthropic-Pentagon confrontation under a headline that cut to the bone: "Privacy Protections Shouldn't Depend On the Decisions of a Few Powerful People."

Sit with that for a moment. The EFF was not criticizing Amodei for refusing the Pentagon. It was criticizing the structural arrangement that made his refusal the only thing standing between mass surveillance and the American public. The problem wasn't the decision. The problem was that the decision rested with one person, running one company, whose values happened to include a commitment to civil liberties.

What if the next CEO didn't share those values? What if Anthropic's board, under pressure from investors who had poured over $67 billion into the company across seventeen funding rounds, decided that Pentagon contracts were too lucrative to refuse? What if the $380 billion valuation made the company too big to stand on principle?

This is the paradox at the center of the safety argument, and it maps precisely onto the paradox that has run through this entire book.

The open-source movement was created to prevent exactly this kind of power concentration. Richard Stallman's original insight, which we explored in Chapter 3, was that proprietary software creates dependency: when one entity controls the tools you need, your freedom exists only at their discretion. The copyleft licenses, the free software ethos, the entire four-decades-long struggle for software freedom was aimed at ensuring that no individual, no corporation, no government could hold the digital commons hostage.

Now the safety argument was inverting that logic. It was saying: this technology is so dangerous that someone must control it. Open release is too risky. The genie cannot go back in the bottle once it's out. Therefore, control — corporate control, centralized control, the antithesis of everything the free software movement fought for — is not just acceptable but necessary.

And the evidence was not trivial. Amodei's five risk categories were not hypothetical nightmares. Biological misuse was a concrete and imminent concern. Authoritarian consolidation was already happening in countries deploying AI-powered surveillance. Economic disruption at the scale Amodei described would destabilize democracies. These were real risks, documented by researchers across the political spectrum.

But the counter-evidence was equally real. Mozilla's Joint Statement on AI Safety and Openness, signed by more than 1,800 researchers and practitioners, argued that increasing access to AI models would ultimately make them safer — that transparency and collective scrutiny would find vulnerabilities faster than any closed team could. The history of cybersecurity overwhelmingly supported this view. Security through obscurity — the practice of keeping systems safe by keeping them secret — had been debunked so thoroughly that it was practically a punchline in the security community. Open protocols, open code, open review: these were the foundations of every secure system that actually worked.

The 2025 International AI Safety Report had found wide disagreement among experts on the fundamental questions. There was no scientific consensus on the likelihood of losing control over advanced AI systems. There was no scientific consensus on the risk of AI-driven manipulation. The honest answer to the question "are frontier AI models too dangerous to release openly?" was: we genuinely don't know.

And yet decisions had to be made. Models were being built. Capabilities were advancing. The luxury of waiting for scientific consensus did not exist.

---

## The Decade We Didn't Take

There is a question this chapter must ask, even though the open-source movement does not want to hear it.

Open source accelerated AI development by years — perhaps by a decade. PyTorch, released by Meta in 2016, became the de facto standard for deep learning research by 2020. TensorFlow, Hugging Face's Transformers library, the open publication norms that allowed Google's "Attention Is All You Need" paper to launch the transformer revolution — each of these was an act of openness that compounded into the fastest capability explosion in the history of technology. Yann LeCun, Meta's chief AI scientist, has stated plainly: "The risk of slowing AI is much greater than the risk of disseminating it." The entire AI ecosystem is built on the premise that faster is better and open is faster.

But this book — a book about a species acquiring power faster than it can build the responsibility structures to hold it — must ask: what if slower would have been better?

Not because closed is superior to open. The safety-through-obscurity argument has been debunked in every other domain. Not because corporations should control AI — the concentration-of-power risks are real and documented. But because *time* is the variable the species needs most, and the open-source movement traded time for speed without asking whether speed was what the situation required.

A decade of slower AI development would have been a decade in which governance could have caught up. A decade in which the safety research could have matured before the capabilities outran it. A decade in which societies could have deliberated about what they wanted from artificial intelligence before artificial intelligence was already reshaping their economies, their politics, their children's attention, and their labor markets.

The open-source movement's deepest conviction — that openness is always preferable to closure, that more access is always better than less — was forged in the world of text editors and operating systems. In that world, the conviction was correct. A text editor cannot cause civilizational harm. An operating system does not pose existential risk. The four freedoms — to run, study, redistribute, and modify — were and remain genuine goods when applied to software that is bounded in its potential impact.

But AI is not bounded. And the framework that was designed for bounded software has been applied, without modification, to unbounded capability. The same CC BY-SA license covers a recipe blog and a frontier model's weights. The same "freedom to redistribute" applies to a calculator app and to a system that can generate novel pathogens. The open-source framework has no mechanism for distinguishing between them, because it was designed in a world where the distinction did not exist.

This is not an argument for closure. It is an argument for what the Grammars book calls *responsibility structures* — constraints that match the power of the thing being released. Open the costs side: infrastructure, tooling, standards, safety research, the shared commons that everyone needs. Hold the revenue side accountable: the model weights that generate market power, the deployment at scale, the thing that directly amplifies human capability beyond human oversight. Not closed — but open with obligation. Licensing that carries responsibility, not just permission.

The analogy: we open-source building codes — everyone benefits from safer buildings. We do not open-source the right to build skyscrapers without inspection. The building code is the grammar. The inspection is the responsibility structure. You need both.

---

## The Alignment Stack

Beneath the political drama of the Pentagon confrontation lay a quieter, deeper problem — one that Constitutional AI had surfaced without solving.

Every AI model that interacts with humans embodies a set of values. Those values are encoded through training: what data the model learned from, what behaviors were reinforced, what principles were written into its constitution. The question of whose values get encoded is not a technical question. It is a political one.

Anthropic's Constitutional AI was more transparent about this than any alternative. You could read Claude's constitution. You could see the priority hierarchy: safety, then ethics, then company guidelines, then helpfulness. You could trace the intellectual lineage from the UN Declaration of Human Rights through Anthropic's internal research to the specific principles the model was trained to follow. This transparency was genuine and valuable.

But transparency about the process does not resolve the fundamental question of legitimacy. Who gave Anthropic the authority to decide that safety should rank above helpfulness? Who decided that the UN Declaration's values — products of a specific historical moment, shaped by Western liberal democracies in the aftermath of World War II — should form the ethical foundation for a global technology? Who decided that a small team of researchers in San Francisco should be the ones making these choices at all?

The question was not rhetorical. It had concrete implications. Anthropic's constitution reflected particular values: liberal democratic norms, individual rights, a specific conception of harm. These values are defensible. Many people share them. But they are not universal. A model trained on Anthropic's constitution would behave differently in contexts where those values conflicted with local norms — and the model would be deployed globally, in cultures and political systems that had no input into the principles it followed.

Anthropic had attempted to address this through experiments in what it called Collective Constitutional AI — projects that sought public input on constitutional principles. But these were experiments, not governance structures. The final decisions about what went into the constitution remained with Anthropic. The company was, in effect, a constitutional convention of one — drafting the foundational values for a technology that would touch billions of lives, with no electoral mandate, no democratic accountability, and no mechanism for the governed to alter the governing document.

This is not a critique of Anthropic specifically. It is a critique of the structural arrangement that the safety argument inevitably produces. If you accept that AI models need value alignment, and if you accept that value alignment requires centralized control over the training process, then you have accepted that a small number of organizations will encode the values that govern a technology used by billions of people. You have accepted, in other words, the very concentration of power that the open-source movement was designed to prevent.

<!-- PP: This is the philosophical heart of the chapter. The "constitutional convention of one" line is strong. Consider whether this section should be longer — it's the argument that separates this book from a standard AI policy analysis. -->

---

## The Tension That Cannot Be Resolved

The safety argument and the openness argument are both correct. This is the uncomfortable truth that Part IV of this book is built around, and that this chapter must make explicit.

The safety argument is correct that AI systems of sufficient capability could enable catastrophic harm. The evidence for biological misuse risk is strong and growing. The authoritarian surveillance risk is not hypothetical — it is already deployed. The economic disruption risk is plausible on timelines short enough to matter. These are not corporate scare tactics. They are assessments shared by researchers at universities, nonprofits, and government agencies with no financial interest in keeping models closed.

The openness argument is correct that concentrating control over the world's most powerful technology in the hands of three or four corporations is dangerous in its own right. History provides no examples of concentrated technological power being wielded exclusively for the public good over the long term. Corporations respond to shareholders, to markets, to the political environment. Anthropic's refusal of the Pentagon was admirable — and it was one board vote away from going the other way. Safety commitments erode. RSP v3.0 proved it.

The tension between these two truths cannot be resolved by choosing one side. It can only be navigated. And the navigation requires being honest about what each side gives up.

If you choose safety through control, you give up the distributed resilience that open systems provide. You create single points of failure — technical, ethical, and political. You trust that the companies and governments wielding control will continue to deserve that trust, despite every historical precedent suggesting otherwise.

If you choose openness, you give up the ability to prevent worst-case scenarios through access control. You accept that bad actors will use openly released models for harmful purposes, and you bet that the benefits of collective development — faster vulnerability discovery, broader safety research, democratic participation in value alignment — will outweigh those harms.

Neither choice is safe. Both involve accepting significant risk. The difference is in where the risk is concentrated: in the hands of the few, or distributed across the many.

---

## A Bridge to the Frontier

One month before the Pentagon confrontation, while Amodei was writing about technological adolescence, the company that had started this entire conversation made a move that suggested a possible middle path.

In January 2026, OpenAI — the organization whose aggressive scaling had driven the Amodei siblings to leave and found Anthropic — announced GPT-OSS, its first genuinely open-source model release in years. Not open weights with a restrictive license, like Meta's Llama. Not a research artifact released for academic study. An open-source model with open training code, released under terms that the Open Source Initiative could actually recognize.

The announcement raised a question that the safety argument, in its purest form, could not answer: if the company that had pioneered frontier AI development was now willing to release capable models openly, had the safety calculus changed? Was there a way to be open behind the frontier — releasing models that were powerful enough to be useful but not so powerful that they posed catastrophic risk?

Or was this just the latest iteration of the strategic openness that this book has tracked through every chapter — giving away what no longer provides competitive advantage, while keeping the crown jewels locked away?

The next chapter takes up that question.

<!-- PP: Chapter 11 will cover OpenAI's GPT-OSS release and the "open behind the frontier" concept. Make sure this bridge doesn't give away too much of that chapter's argument. Just plant the question. -->
