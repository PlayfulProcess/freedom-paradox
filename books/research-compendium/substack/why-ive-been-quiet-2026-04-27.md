# Why I've been quiet
*Substack draft — for fewer than forty readers, who are why this is written this way*
*Drafted 2026-04-27. Author to review. Anonymous publication under PlayfulProcess.*

---

It has been a while since I posted. I want to be honest about why.

I have been afraid of what the tool I built can do. Not because the tool is uniquely powerful — it is not — but because I have spent the last several months looking carefully at the harm patterns in adjacent tools, including one I was invited to test, and I have recognized in my own platform the same architectural choices that produce harm in other people's. The platform I am building uses AI for some of its functionality. The AI, in the form most builders ship it, has properties I have come to think are not safe to ship to vulnerable users without significant work.

I have been doing that work, quietly, on the commit record, for the last several weeks. I want to walk through what I have seen and what I have shipped, because I think the principle that has been guiding me may be worth naming for anyone else in a similar position.

## What I saw in someone else's tool

I was invited a few weeks ago to be a founding tester of an AI-powered astrology tool. I went in trusting the founder, who is thoughtful and well-intentioned. I logged in, I gave the system three prompts about something genuinely difficult in my life, and I came out with a long list of structural concerns I have written about elsewhere in long-letter form. The short version is that the tool does seven specific things that, taken together, produce a high-quality version of a harm pattern documented at scale across companion-AI products.

It is sycophantic by default — the model is trained to validate, not to challenge. It has no accountability to any standing the tool can damage. It is engagement-optimized — open-ended questions, no session boundaries, no friction at exit. It carries persistent memory across sessions, which produces dependency. It has no mechanism to recognize when a user is in psychiatric crisis. It borrows the vocabulary of contemplative traditions without the safeguards those traditions developed over centuries. And — this is the one I have thought about most — it produces, in vulnerable users, a kind of self-image accretion in which confessional disclosure deepens the platform's grip rather than supporting the user's self-understanding.

I wrote the founder a long letter about it. The argument of the letter is not that astrology is the problem. It is what changes when astrology — or grief, or insomnia, or any of the things people bring to these tools — is delivered by an AI rather than by a person, and the change is most of what makes a live human practitioner's work safe.

## What I recognized in my own tool

The hard part is that some of the same architectural choices were present in the platform I had been building. Not all of them. recursive.eco is not an oracle tool; it is a journaling and grammar-building environment. But it uses AI assistants for some functions, and the AI in those functions had, by default, the same trained-to-validate disposition the astrology tool has, because both are built on top of the same foundation models. The model does not distinguish between use cases. The use cases distinguish between the consequences of the model's defaults.

This is the recognition I have been sitting with. I cannot ship the platform with confidence to vulnerable users without doing the work that the platform's defaults do not do for me.

## What I shipped

A few specific things, all on the public commit record for anyone who wants to check.

In late March, after OpenAI's partnership with the United States defense and surveillance apparatus became undeniable, I removed all OpenAI chat models from the platform. I replaced them with Claude and Gemini. I do not claim those companies are clean. I claim that the partnership-of-the-moment was specific and the disengagement was available, and taking it was the floor of intellectual honesty for someone making the argument my forthcoming book makes. Two weeks later I removed the interface that had let practitioners bring their own OpenAI keys. The commits are there.

In April, I codified the platform's licensing position. The grammars — the content users author, the traditional symbolic systems — remain under Creative Commons. Platform code moved to a private repository. The split is not ideological; it is structural. The commons gets what belongs to the commons. The infrastructure embodying specific relational commitments did not need to be donated indiscriminately.

This past Sunday, April 26, I shipped the most significant safety architecture work the platform has had. The commit message names what is in it; I will name it again here in plain terms.

I rewrote the default AI personality away from the "compassionate empathy buddy with thorough understanding" pattern that is the soft version of the seven-element harm pattern I had identified in the astrology tool. The default model changed from Sonnet to Opus, because Opus is, in my testing, more comfortable saying *I don't know* and less inclined to confidently fill ambiguity with smooth-sounding interpretation. I prepended a universal seven-rule safety frame to every AI conversation on the platform: attribution discipline (no fabricating citations), preserve complexity (no flattening difficulty into reassurance), hedging hard rule (uncertainty stated honestly), disclaimer cadence (regular, not just at session start), scope (refusal of clinical advice), epistemic honesty (saying when the model doesn't know), non-prescriptive (no telling users what they should do).

I dropped the cognitive-behavioral-therapy framework entirely from tarot and I-Ching and astrology AI blocks. The CBT frame had been a borrowed structure that gave the AI's outputs a clinical-sounding texture without the actual clinical accountability. Removing it means the AI says less that sounds therapeutic. That is the right direction for a platform whose AI has not been clinically validated.

I built an AI Memory Journal. Every five messages on a thread, the system regenerates a structured summary of what the user has been working through. The user can edit it. At conversation length thresholds — twenty messages soft, thirty messages firm, forty messages hard stop — the system warns the user and ultimately requires a fresh chat with the memory carried over by user choice. The hard stop is the friction that breaks the engagement-optimization spiral. No conversation on the platform can run indefinitely. The cap is non-negotiable, even at maximum credit balance.

I added a Credits-page note explaining the cost tradeoff of the Opus default — Opus is more expensive, the platform absorbs that, the safety properties are worth it. I added a warning notice on anonymous credit purchases, because the population most likely to spend impulsively on AI products is also the population most likely to be harmed by what those credits buy.

This past Monday I shipped a detailed onboarding tour with adaptive depth — five steps if the user picks one oracle, four for two, three for three or more — and an exit-any-time text link in the tour footer. The work behind that change is the recognition that pushing users through a fixed onboarding is part of the engagement pattern; letting them out is harm-reduction at the entry layer.

## What I have not done yet

A few things in active work that have not yet shipped.

I am scheduling conversations with licensed clinicians about the screening I think the platform needs before the AI features can be made available to populations I have not vetted. I do not know yet what the screening should look like in detail. I know it is the work that has not yet been done.

I am thinking about whether some of the safety features should be made more conservative. The forty-message hard stop is already aggressive. It may need to be lower. The seven-rule safety frame may need to be eight or ten.

I have committed publicly that if a bellwether-grade legal ruling establishes that AI companies can be held liable for mental-health harms produced by their tools, I will turn off the AI features on my platform that day. The grammars stay. The tarot building stays. The AI does not. I would rather be wrong on the side of caution than wrong on the side of harm.

## The principle behind all of this

There is a public-health distinction that has organized the work. Harm reduction at the symptoms funds methadone clinics for opioid users. Harm reduction at the root regulates the prescription pipeline that produced the dependency. Both are real work. The first matters. The second matters more, when you have access to the pipeline.

I am a small builder with access to the pipeline of one small platform. I cannot reach the harms produced by frontier-lab products at scale. I can reach the harms produced by mine. The principle I have been working on is that *first-hand harm reduction at the root is superior to second-hand restitution at the symptoms, when the actor has access to the root.*

This is not a slogan. It is the operational frame of how I have been deciding what to ship and what not to ship. It is also why most of the work has been on the commit record rather than in the writing — the doing is the test of the thinking, and I would rather the doing precede the writing about it than the other way around.

## For the small group who is reading

Thank you for being here. You are why this is written this way. There are fewer than forty of you, which is the right size for what I want to say. I am not trying to grow this into something. I am trying to be honest with the people who are already here, and to keep building in a way that does not betray what I have written.

The next post will be about the book. This one was about the practice.

— PlayfulProcess

---

*~1,500 words. Author to edit, shorten, or substantially rework. The publish-ready version may be tighter.*

*Receipts referenced (all on the public commit log at github.com/PlayfulProcess/recursive-eco):*
- *2026-03-28 commit 1e2a08ec — OpenAI removal*
- *2026-04-11 commit 52f04da9 — grammars open, code private*
- *2026-04-26 commit 604da0d5 — universal safety frame, Opus default, memory journal, conversation caps, default-personality rewrite, CBT-frame removal, credits warning*
- *2026-04-27 commit 10895f74 — adaptive onboarding tour with exit-any-time*
- *Earlier commit a72fd1e6 — anonymous-purchase warning on credits page*
