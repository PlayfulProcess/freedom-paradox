# Chapter 1: Take the Argument Seriously

---

In May 2023, Geoffrey Hinton resigned from Google so that he could speak freely about the risks of the technology he had spent his career building. He was seventy-five. He had just received the Turing Award — the closest thing computer science has to a Nobel — for the neural network research that made the current AI systems possible. He had trained, among others, Ilya Sutskever, who went on to co-found OpenAI. In the interview he gave to *The New York Times* that week, he said he regretted his life's work. He said the systems he had helped build might, within a span of years, become capable of outthinking their designers. He said the people building the most advanced versions of those systems were, in his estimation, moving too fast to be careful.

The statement was reported. It was discussed for a week. Then the news cycle moved on. Google's stock did not move. The labs did not slow down. Hinton gave further interviews. The Doomsday Clock, maintained by the Bulletin of the Atomic Scientists, was moved forward the following January, citing AI as one of the reasons. The labs did not slow down.

Yoshua Bengio, another Turing Award winner, another original architect of deep learning, rearranged his professional life in the same period to focus full-time on AI safety. He had testified before the U.S. Senate. He had co-authored the International AI Safety Report. He had said, in a public letter signed by hundreds of researchers, that there is a non-trivial probability that advanced AI systems could pose an existential risk to humanity. He said it carefully, with caveats, in the way that a senior scientist says things. The labs did not slow down.

Stuart Russell, who wrote the standard undergraduate textbook on AI — the one most working researchers learned from — wrote a second book in 2019, *Human Compatible*, arguing that the entire field had been built on a foundational error: that optimizing for a specified objective is a good paradigm for building systems more capable than us, when in fact it is the paradigm most likely to get us killed. He has been on podcasts. He has briefed governments. The textbook is still the textbook. The field has not restructured itself around his critique. The labs did not slow down.

Eliezer Yudkowsky, who has been making some version of this argument for twenty years, wrote an op-ed in *TIME* magazine in March 2023 calling for an international moratorium on frontier training runs, backed by willingness to destroy non-compliant datacenters by military force. He was widely mocked. He was also, at the same time, widely read. In 2025 he and Nate Soares published *If Anyone Builds It, Everyone Dies* — a title chosen, presumably, to resist further softening. The book is not a hedge. The book says what the title says. It was reviewed. It was discussed. The labs did not slow down.

---

I am going to state the thing plainly, because the rest of this book depends on you accepting it as a premise rather than debating it as a hypothesis.

The people who built this technology, and the people who most carefully study it, are — in non-trivial numbers — saying it might kill everyone. Not "disrupt labor markets." Not "spread disinformation." Not "concentrate power in undemocratic ways," though they are saying those things too. They are saying: it might kill everyone. They are saying this in public. They are signing letters. They are leaving jobs to say it. They are testifying to legislatures. They are writing books with titles that do not permit softening.

This is not a fringe position. It is not held only by outsiders. It is held, in varying strengths, by people inside the labs. Dario Amodei, the CEO of Anthropic, has said in multiple public interviews that he thinks the probability of catastrophic outcomes from advanced AI is in the range of ten to twenty-five percent. Demis Hassabis, the CEO of DeepMind, has signed the statement that says AI extinction risk should be treated as a societal-scale priority on par with pandemics and nuclear war. Sam Altman, the CEO of OpenAI, has said similar things in different registers at different times. These are not the CEOs of tobacco companies denying that their product causes cancer. These are the CEOs of the companies building the thing, saying that the thing they are building might destroy the world, and continuing to build it.

In any other context, that number — ten to twenty-five percent chance of catastrophic outcome — would halt the activity. We do not get on airplanes with a one-in-a-million chance of crashing, let alone one in four. We do not eat food with a one-in-ten chance of being fatally contaminated. We do not, as a society, tolerate that level of risk in almost any domain we regulate. But we tolerate it in this one. The activity has not halted. The activity is accelerating.

This book asks why.

---

It does not ask the question the way previous books have asked it.

It does not ask *is the risk real*. That question has been asked. Books have been written on each side. The argument has, in a sense, been had. This book will summarize the argument in the next chapter, briefly, so that a reader who has not been tracking it has the map. But the argument will not be the subject of the book. The argument has not been won. The argument has been *bypassed*.

It does not ask *what should policy do*. That question has been asked by more qualified people. Yudkowsky and Soares have a policy proposal. Russell has a policy proposal. Bengio has a policy proposal. The proposals differ in detail. The policy community knows what the proposals are. No serious policy motion is occurring in the direction of any of them. This book will briefly note why, and move on.

It does not ask *how to solve alignment*. I am not an alignment researcher. Nothing in this book will help anyone solve alignment. If alignment is solvable, it will be solved by people with technical skills I do not possess, working on problems I do not understand well enough to describe.

The question this book asks is the one that remains after all of those questions have been asked and not answered.

*Why is the argument not landing?*

The argument is clear. The evidence for taking it seriously is substantial. The people making it are credentialed, careful, and consistent. The stakes are maximal. The activity being argued against is not, in the conventional sense, forced — no military requires it, no law mandates it, no person would die tomorrow if it stopped. And yet it continues, and accelerates, and the people most concerned about it use the products of the activity in their daily lives, and the people least concerned about it regard the concerned people as a fringe, and the policy conversation never reaches the point of substantive intervention.

This is a strange thing. It wants explaining.

---

A note about what I am and am not saying.

I am not saying Yudkowsky is right. I have no probability of doom to offer you. I have been close enough to the people making these arguments, on both sides, to know that honest people disagree, that the honest uncertainty is large, and that anyone who offers you a specific number is either confused or selling something. I will not offer you a number.

I am not saying the labs are evil. I am on record, in this book and in my own life, as someone who uses their products, pays them money, and builds on top of their systems. The people who work there are, in my experience, thoughtful and often anguished. The Anthropic safety team is staffed by people who genuinely worry about the thing they are building. The OpenAI superalignment team existed, and its members resigned in protest, and some of them resigned into positions at Anthropic, where they continued trying to solve the same problem from a different company's payroll. These are not people acting in bad faith.

I am not saying we are doomed. I do not know if we are doomed. The case for thinking we might be doomed is strong enough that a reasonable person should take it seriously. The case for thinking we are probably fine is not strong, but it is not absent either. Reasonable people hold both.

I am saying something narrower and, I hope, more useful. I am saying: given the state of the argument, the activity should already be different than it is. Not "shut down." *Different.* Slower, more coordinated, more cautious, more publicly accountable, more willing to pause at specific thresholds, more willing to treat its own employees' stated concerns as data rather than PR problems. The gap between where the activity is and where the argument would predict it should be is a gap that demands explanation.

The explanation is not "the argument is wrong." The argument has not been refuted. The explanation is not "the people making the argument are stupid." They are, on the contrary, among the most intelligent people working in the field. The explanation is not "the information has not reached the decision-makers." The decision-makers are, in many cases, the people who first made the argument.

The explanation is somewhere else. The explanation is in the gap between what a human nervous system can hold and what this particular argument requires it to hold. The explanation is in the stories the people inside the activity tell themselves to make the activity bearable. The explanation is in the particular way that geopolitical framing converts individual choice into collective compulsion. The explanation is in how the product is good enough, beautiful enough, useful enough, that turning against it feels like turning against something one loves.

The explanation is in the anthropology of the failure, not in the logic of the argument.

That is what this book is about.

---

One more thing before we begin.

I am, myself, a builder inside the ecosystem I am describing. I pay for Claude. I use it to write this book. I have built a small platform on top of Anthropic's API, and every user I onboard is a few more dollars routed to the company whose product I am, in these pages, describing as possibly civilization-ending. I am not outside the pattern. I am inside it. I could not write this book without the tools I am describing as potentially catastrophic.

This is not a disclosure I am making reluctantly. It is, I will argue, the structural condition of almost everyone currently in a position to think seriously about the problem. The people outside the ecosystem do not know enough about the technology to evaluate the claims. The people inside the ecosystem are, by virtue of being inside, implicated in the activity. There is almost no epistemically clean position. The choice is between informed complicity and uninformed distance. This book is written from informed complicity, because I have come to think that the alternative is worse — that uninformed distance produces worse diagnoses than complicit attention.

But I want to name the complicity clearly at the start, because any honest account of why the argument is not landing has to include the author in the account. I am part of the mechanism I am describing. Chapter 7 of this book is about that. The rest of the book is about the larger version of the same mechanism, visible in other people, at larger scales, with more money and more consequence. I am a small node in the thing. But I am a node, and pretending I am not would be the first move of the machinery this book is trying to see.

So: take the argument seriously. Not because I am asking you to agree with any particular probability of doom. Because the people most qualified to have a view are, in non-trivial numbers, saying what they are saying, and the activity is continuing as if they were not, and that gap is the thing worth understanding.

The next chapter will lay out what Yudkowsky and the others are actually saying, stripped of the rhetoric and the hostile summaries, so that what follows can be discussed on the basis of the real claim rather than a caricature of it. Then we will turn to why the claim is not landing, which is the subject the rest of the book will spend itself on.

---

*CC BY-SA 4.0*
