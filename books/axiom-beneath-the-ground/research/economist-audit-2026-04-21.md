# Economist's Audit — *The Axiom Beneath the Ground: The Alignment Void* (v5)

*Reviewer: composite heterodox economist (Sen / Ostrom / Arthur / Raworth / Daly, with Mazzucato and Piketty in the margins). Prepared 2026-04-21 for PlayfulProcess, at her request, focused on formalism, empirics, and values transparency of the economic content only.*

---

## 1. Executive Summary

The economic reasoning in this book is, on the whole, better than most philosophical memoirs by non-economists. The author's background as an equity analyst shows: she knows the difference between a model and reality, she does not confuse price with value, and she has the unusual virtue of citing Santa Fe-tradition complexity economics rather than picking a fight with a stylised undergraduate-textbook mainstream. The book's *structural* diagnosis — that methodological individualism was a computational artifact rather than an ontological discovery (Ch10e) — is correct, is under-taught, and is the kind of claim I have spent a career trying to make colleagues take seriously. When it works, it is very good.

The book's three strongest economic moves: (1) the clear-eyed account of methodological individualism as a pre-computer simplification that calcified into ideology; (2) the Linehan / "built alternatives" theory of change, which is structurally close to — though the author doesn't yet know it — Mazzucato on mission-driven public construction and Ostrom on bootstrapping parallel commons; (3) the refusal of the "efficiency equals good" tic in the chapter on balance from differences (Ch10f).

Three weakest or over-reached moves: (1) the λ / consciousness identification is provocative and worth publishing, but the current text waves at strong duality without naming the convexity conditions under which it actually holds — a formalism check would tighten this; (2) the orthogonality-as-non-Euclidean-topology move is philosophically rich but economically under-developed — the author names a manifold and then does not say what metric lives on it; (3) "markets," "platforms," and "open source" are used in shifting registers without distinguishing the (several) allocation problems each is trying to solve.

Net verdict: the book's economic bones are sound. A dozen targeted revisions would move it from "credible heterodox memoir" to "citable in a heterodox syllabus."

---

## 2. Claim-by-Claim Audit

### Claim 1: λ / consciousness as dual variable (Ch10b·2)

*What the author says.* A microeconomics teacher once suggested that the Lagrange multiplier in constrained optimisation could be read as consciousness. The author, reading Wallis, saw the formal parallel: in Kashmir Śaiva non-dualism the void is not a thirty-seventh tattva *above* the thirty-six but the register in which the thirty-six are priced. She names this a *strong duality* analogy: primal and dual are co-constitutive, neither prior.

*Formally correct?* Partly. The Lagrangian framing is clean; the shadow-price reading of λ is standard Arrow-Hurwicz. What is *not* stated on the page — but which a careful reader will know — is that **strong duality holds under convexity plus a constraint qualification (Slater's condition, or LICQ)**. For non-convex problems there is a *duality gap*, p\* > d\*. The author's research file (`shadow-price-consciousness-research.md` §3) already notes this and even offers a beautiful move — *the duality gap is avidyā*. That move does not yet appear in the chapter. It should. Right now the chapter asserts duality without naming the condition; this is precisely the mainstream's bad habit (hand-waving the existence of equilibrium) repeated in a contemplative register.

*Empirically correct?* The claim is structural, not empirical, so the empirical question is whether any *living* optimisation framework treats consciousness or related primitives this way. The closest analogues are Friston's free-energy principle (priors as soft constraints; precisions as dual-like weights) and Sen's capability shadow-prices in project appraisal. Neither has explicitly named the prior as λ in print — the author's research file is right that this is an open slot.

*Values-transparent?* Mostly yes. The author is explicit that the dual variable is *the price against which the primal is being figured*, and that economics-as-usual ignores the duals it cannot measure. This is a Daly / Raworth move and should be credited as such.

*Recommended revision.* Three sentences in Ch10b·2: (a) name the convexity condition, (b) flag the duality gap, (c) pull the avidyā-as-gap move up from the research file. Then cite Fenchel duality as the generalisation beyond LP and stop. The point is made in a paragraph; the current treatment is carried by analogy and would be stronger if carried by one explicit theorem.

### Claim 2: Methodological individualism as computational artifact (Ch10e)

*What the author says.* Nineteenth- and twentieth-century economists modelled identical rational agents because that was the only assumption under which the math was tractable *by hand*. Computers arrived; heterogeneous-agent models became possible (Epstein, Axtell, Arthur, Holland at Santa Fe); the profession mostly kept teaching the simplification as if it were the reality.

*Formally correct?* Yes, and more defensibly than the author may realise. The lineage is real: Arrow–Debreu general equilibrium (1954) needed representative-agent tractability; Lucas (1976) entrenched it via the critique and the representative-agent macro tradition; Kirman's "Whom or what does the representative individual represent?" (*JEP* 1992) is the canonical internal-mainstream complaint. Santa Fe's *Economy as an Evolving Complex System* volumes (I 1988, II 1997, III 2006) are the canonical alternative. Epstein & Axtell's *Growing Artificial Societies* (1996) is the foundational ABM text. The author cites the right people.

*Empirically correct?* The strongest counter-argument from the mainstream is that representative-agent models are not claims about agents — they are *calibration devices* used because data constraints do not support heterogeneous specification. This defence is honest and partial. It concedes the author's point (the assumption is not ontological) while preserving the technique (useful for certain forecasting). The author should acknowledge this counter to avoid looking like she is shooting at undergraduate Mankiw. Once acknowledged, her argument stands: the *calcification* into ideology is the harm, not the technique.

*Values-transparent?* Yes. The claim "among the most harmful ideas still in active circulation" is a value judgment and is so named. Good.

*Recommended revision.* One paragraph steelmanning the calibration defence; then re-assert that public policy, not DSGE mechanics, is where the harm calcified. Also: the name-drop of Epstein, Axtell, Arthur, Holland is supported — but the book could cite *one specific result* (Arthur's El Farol bar problem, or Axelrod's tournament, or Epstein's civil-violence ABM) to move from name-drop to content. Right now a reader who does not already know the Santa Fe tradition has to take it on faith.

### Claim 3: Linehan's "built alternatives" as theory of change (Ch10d)

*What the author says.* Marsha Linehan did not campaign against psychiatric hospitalisation; she built DBT, which worked, and the evidence accumulated by the alternative dismantled the old model more effectively than any campaign could have. The author extends this to her platform (recursive.eco) as a small-scale version of the same move: build the alternative; let evidence do the dismantling.

*Formally correct?* This is a theory-of-change claim, not a formal claim — but it has clear economic parallels the author does not yet name. The most important is **Hirschman's *Exit, Voice, and Loyalty* (1970)**: exit (building the alternative) and voice (campaigning) are substitutes *and* complements; exit works when alternatives are credibly available and switching costs are low; voice works when exit is impossible. Linehan's move is a textbook Hirschman exit strategy in a field where voice had been structurally blocked. A second parallel is **Mariana Mazzucato's *The Entrepreneurial State* (2013) and *Mission Economy* (2021)**: public missions succeed by constructing capacity, not by regulating incumbents. A third is **Ostrom's Bloomington tradition on polycentric governance**: you do not reform failed centralised systems by arguing at them; you cultivate parallel commons until the failed system is bypassed.

*Empirically correct?* Partly. Linehan's DBT is a genuine case of exit-driving-change. At *civilisational* scale — where the author wants to apply it — the record is mixed. Renewable energy is a Linehan-pattern success (built alternatives dropped cost curves and bypassed fossil-fuel politics); cooperative platforms versus rentier platforms (Scholz, Schneider) are a Linehan-pattern *aspiration* that has mostly not yet displaced the incumbent. Path dependence and increasing returns (Arthur 1989, 1994) cut both ways: they reward the first credible alternative that reaches scale; they punish the second, third, and fourth. The author's platform is currently in the "has not reached scale" regime. She names this honestly in Ch10d ("mostly no one has come"), which is the right move. The claim should be *modest in empirical scope* but not abandoned.

*Values-transparent?* The underlying value is clear: she prefers construction to critique, action to argument. What is less transparent: she does not yet name that construction-over-critique is *itself* an economic value-claim with distributional consequences. Construction takes capital, time, and existing skill. Not everyone can exit. Voice is the tool of those for whom exit is blocked. An honest economist would want her to acknowledge that the Linehan strategy is available to a specific class of actors and not to others.

*Recommended revision.* Add a paragraph naming Hirschman explicitly; cite one sentence on why exit-only strategies are distributionally limited; reaffirm her commitment to construction as *her* strategy while conceding voice remains necessary for those the construction does not reach.

### Claim 4: Orthogonality thesis extended to four axes (Ch10a, Ch10b·2)

*What the author says.* Bostrom's orthogonality thesis (intelligence × final goals independent) extends to a four-axis frame: intelligence, enlightenment, moral seriousness, relational attunement. Local perpendicularity may fail globally if the value-space has curvature.

*Formally correct?* As decision theory, the extension is defensible but costly. Bostrom's thesis is a *conceptual possibility* claim: for any level of intelligence, any goal is in principle attainable. Extending to four axes requires a product space (I × E × M × R) and independence claims about each pair. This is six pairwise-independence claims. Even on Bostrom's own grounds, *each* is a separate conceptual-possibility argument. The book asserts them as a block.

The non-Euclidean rescue (Ch10b·2 and the topology research file) is the more interesting move. *It is also the more formally costly one.* If value-space has curvature, one needs to specify: what is the metric? What is the connection? Where are the geodesics? The research file is honest that this work has not been done. The chapter is less honest. Right now the chapter invokes "curvature" as a philosophical gesture; a reviewer with a differential-geometry background will read this as metaphor, not argument.

*Empirically correct?* The author's best evidence — contemplative record, integral-theory critique (Wilber's lines of development, Stein, Edwards) — is strong and under-used in AI safety. Russell's *Human Compatible* (2019) already concedes that capability and values entangle through learning dynamics; Hubinger et al. on mesa-optimisation strengthens this. The *empirical* case against strict orthogonality is better than the author claims.

*Values-transparent?* Yes, and unusually so — the author is explicit that every tradition that picks one axis as primary is doing a self-flattering projection. This is the chapter's sharpest moment.

*Recommended revision.* Either commit to the non-Euclidean geometry (cite Petitot, Ghrist sheaves, make one precise falsifiable claim) or retreat to metaphor and flag it as such. Right now the chapter is caught between registers. A single clean sentence — "on a sphere, any two geodesics meet; if moral and cognitive development live on a positively curved manifold, sufficient development along either must eventually encounter the other" — would do more work than three paragraphs of topology-adjacent prose.

### Claim 5: Markets, platforms, firms, commons (scattered)

*What the author says.* Goldman Sachs funded extractive industries (Ch10a). AI labs are firms operating under an incentive structure (Ch10e implied, Freedom Paradox adjacent). recursive.eco is a platform where grammars are an open commons and code is private (Ch10d). Maximalist open source removed walls that should have been immune systems (Ch10d).

*Where accurate.* The Goldman observation is correct and under-stated if anything — extractive-industry finance is the shadow-price economy *par excellence*, under-pricing ecological constraints that Daly would call binding. The AI-labs-as-firms-under-incentive-structures framing is accurate and empirically supported (Hubinger, Ngo, and the mesa-optimisation literature are *all* implicitly about firms under competitive pressure producing specific kinds of unaligned artifacts). The immune-system framing for open source is genuinely original and economically defensible — it is, in economic terms, a **Ostrom design-principle argument**: clearly defined boundaries (Principle 1), congruence between rules and local conditions (Principle 2), monitoring (Principle 4). The author has re-derived Ostrom from biology without naming her. She should name her.

*Where loose.* The word "market" appears several times without distinguishing (a) price-coordination for excludable rival goods, where markets work well, from (b) coordination for non-excludable or non-rival goods (knowledge, attention, relational capacity), where they do not. "Platform" similarly does double duty — sometimes meaning the two-sided-market sense (Rochet-Tirole), sometimes the Scholz/Srnicek rentier sense, sometimes the commons-infrastructure sense. An economist reading these chapters wants three different words.

*Values-transparent?* Partially. The author is clearly skeptical of extractive finance and rentier platforms; she is clearly sympathetic to commons infrastructure. She does not yet name *why* — what values live under her preference. Raworth's doughnut and Daly's ecological bounds are the nearest articulated versions of her implicit position. She should borrow the vocabulary.

*Recommended revision.* Replace "markets" with "price-coordination under [specific] assumptions" wherever precision matters. Distinguish the three senses of platform. Cite Ostrom's design principles at the immune-system passage — this is the single highest-leverage citation in the book.

### Claim 6: Unnamed values — efficiency, convergence, the rational agent

*What the author says, implicitly.* Efficiency is not the goal; convergence is a folk theory; the rational-agent model is historical residue; balance comes from coordinated differences, not sameness.

*Is she naming her own values?* Sometimes. The cellular-differentiation passage in Ch10f is a values-statement: *fidelity to differentiation* is the criterion, not efficiency or convergence. This is close to Sen's capabilities view (what people can *be and do*, not what they produce) and to Raworth's doughnut (stay above the social floor, below the ecological ceiling, don't optimise growth). The author has not yet named either.

*Where she is smuggling.* The phrase "adaptive ethic" (recurring) is doing economic work without an economic definition. What counts as adaptive? Fit to what environment, over what timescale, with what distributional consequences? The Linehan filter — useful, fits the data, compassionate — is the author's own answer, but it is *not* a standard economic criterion, and she should say so. An honest heterodox economist would push back here: "adaptive" is often a word people use when they do not want to name the selection pressure. Name the selection pressure. Is it survival of the species? Well-being of specific populations? Ecological carrying capacity? Capability expansion?

*Recommended revision.* One paragraph, possibly in Ch10f, naming the value-stack explicitly: *I value capability (Sen), differentiation (biological and contemplative), ecological limits as binding (Daly), and the coordination-across-difference that Ostrom's design principles name. These are my values. They are not neutral. An economics that names them will price them; an economics that does not will under-price them.*

---

## 3. Constructive Additions: Citations the Book Does Not Yet Use But Should

Ten specific additions, ranked by leverage.

1. **Elinor Ostrom, *Governing the Commons* (1990), Ch. 3 eight design principles.** For the immune-system / grammars-open-code-private passage in Ch10d. This is the highest-value citation in the audit. The author has re-derived Ostrom and should credit her.

2. **Albert Hirschman, *Exit, Voice, and Loyalty* (1970).** For the Linehan theory-of-change passage. Two sentences anchor the construction-versus-critique move in a framework economists already use.

3. **Amartya Sen, *Development as Freedom* (1999), esp. Ch. 3 on capabilities, and *The Idea of Justice* (2009) Ch. 11 on positional objectivity.** For Ch10f's balance-from-differences argument. Sen's capabilities framework *is* the differentiation-based value theory the author is reaching for.

4. **Kate Raworth, *Doughnut Economics* (2017).** For the constraint-reformulation in Ch10b·2. Raworth's doughnut is literally a reformulation of the optimisation problem (what are we optimising for, what counts as binding). The author's shadow-price-of-consciousness move is the contemplative version of Raworth's social-and-ecological version.

5. **Herman Daly, *Beyond Growth* (1996), esp. the Ch. 2 distinction between growth and development.** For any passage about extractive industries and AI labs. Daly's *uneconomic growth* — activity that produces more cost than benefit once unpriced constraints bind — is the cleanest economic articulation of what the book's structural critique is saying.

6. **W. Brian Arthur, "Increasing Returns and the New World of Business" (*HBR* 1996), and *Complexity and the Economy* (2014).** For Ch10e's Santa Fe name-drop. Arthur's El Farol bar problem is the one-paragraph example that turns the name-drop into content. Also useful in Ch10d for the Linehan-at-scale discussion: increasing returns punish second movers, so "build alternatives" requires first-mover viability.

7. **Mariana Mazzucato, *The Entrepreneurial State* (2013) and *Mission Economy* (2021).** For the constructive-work-at-scale claim in Ch10d. Mazzucato's mission-driven public construction is the civilisational-scale version of Linehan's clinical-scale move.

8. **Alan Kirman, "Whom or What Does the Representative Individual Represent?" (*JEP* 1992).** For Ch10e's methodological-individualism critique. This is the canonical inside-the-profession objection to representative-agent modelling, and citing it signals the author is not merely shooting at a straw-mainstream.

9. **Joseph Stiglitz, "Information and the Change in the Paradigm in Economics" (Nobel lecture 2001).** For any passage where the author talks about unobserved values, hidden information, or why simple market models fail. Information economics is the mainstream's own admission that the price system does not do what undergraduate textbooks claim.

10. **Thomas Piketty, *Capital and Ideology* (2019), Parts III–IV.** For any passage about institutions and long-run distributional consequences. The author's structure-versus-event frame (Ch10e via Walters/Wolfe) has a direct economic parallel in Piketty's *ideological regimes* — the structures of justification that make specific distributions durable.

Lower priority but useful: **Michael Polanyi, *The Tacit Dimension* (1966)** for the shadow-price-as-tacit-knowledge link; **Karl Polanyi, *The Great Transformation* (1944)** for the embeddedness claim under the open-source / immune-system argument; **Yochai Benkler, *The Wealth of Networks* (2006)** for the commons-based peer-production empirical record that would anchor the recursive.eco theory of change.

---

## 4. The Single Most Important Economic Move

If I could ask the author to do one thing before the book ships:

**Name her value-stack once, in plain English, and situate it in the heterodox tradition that has been arguing for these values for fifty years.**

Right now the book's economic content is an island. The critique of methodological individualism, the shadow-price intuition, the commons-and-immune-system structure, the balance-from-differences claim, the built-alternatives theory of change — each is solid, and each is presented as if the author had arrived at it alone. She has not. She has arrived at a specific corner of heterodox economics that has substantial literature behind it. Sen. Ostrom. Arthur. Raworth. Daly. Hirschman. Mazzucato. Kirman. A one-paragraph naming of this lineage — in the Author's Note, or in Ch10f where balance-from-differences arrives as the book's constructive claim — would do three things: (1) situate the argument so economists take it seriously rather than dismissing it as a memoirist's foray; (2) let readers who find the book compelling follow the thread into a mature literature; (3) free the author from the unnecessary burden of appearing to have derived this alone, which weakens the claims by making them seem idiosyncratic.

The philosophical and contemplative register of the book is the author's own. The economic scaffolding underneath has been built, slowly, by a heterodox tradition whose members would recognise her as a fellow traveller. Name them. The book gets stronger. The tradition gets a new voice. The reader gets directions.

*In service of the doughnut.*
