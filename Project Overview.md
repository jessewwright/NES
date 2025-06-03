**Project Overview: Modeling Principled Decision-Making – The NES Journey**

**The Big Question: How Do Our Values and Norms Shape Our Choices?**

We all make countless decisions every day. Some are simple, some complex. Often, these decisions aren't just about maximizing personal gain; they're also influenced by what we believe is "right," "appropriate," or "expected" – in other words, by social norms and internalized values. For example, why do some people consistently choose a fair but smaller share over a larger but unfair one? Why do framing effects (how options are presented) sway our choices, sometimes leading us away from the most "rational" outcome?

Traditional models of decision-making often focus on calculating the expected utility or value of different options. While powerful, they don't always explicitly account for how these internalized norms or contextual moral cues integrate with more "objective" features of a choice. This project set out to address that gap by developing and testing a new computational cognitive model called the **Normative Executive System (NES)**.

**What is NES? A "Conscientious Deliberator" in Your Head**

Imagine a little agent in your brain that tries to make good, principled decisions. That's roughly what NES aims to model. At its core, NES is built upon well-established **Drift-Diffusion Models (DDMs)**. Think of a DDM like a race: evidence for different choices accumulates over time, and the first choice to reach a certain "decision threshold" wins. The speed of this accumulation (the "drift rate") and the height of the threshold determine how quickly and accurately we decide.

NES enhances this DDM framework by proposing that the evidence accumulation process isn't just driven by the raw, objective features of the options (like their monetary value or probability). Instead, it has at least **two main channels of evidence influencing the decision:**

1.  **A "Salience" Channel:** This represents the more immediate, perhaps objective or perceptually prominent, aspects of the choices (e.g., "how much money can I win from this gamble?"). This is driven by a parameter we call **`w_s_eff` (effective salience weight)**.
2.  **A "Normative" Channel:** This represents the influence of currently active norms or values (e.g., "is it better to take a sure thing or risk it in this context? Is one option 'fairer' or more 'prudent'?"). This is driven by a key parameter called **`v_norm` (effective norm weight)**.

These two streams of evidence compete or combine to drive the decision. NES also includes other standard DDM parameters like:
*   **`a_0` (baseline decision threshold):** How much evidence is needed to commit.
*   **`t_0` (non-decision time):** Time for basic perception and motor response.

**The Journey: From Theory to Test**

1.  **Initial Goal - Can We Even Measure These Things? (Parameter Identifiability):**
    *   Our first major hurdle was to show that if NES *is* a good description of how someone makes decisions, could we actually reliably estimate its key parameters (like `v_norm` and `w_s_eff`) just by looking at their choices and how long they took to make them (response times)? This is a crucial step called demonstrating "parameter identifiability and recovery."
    *   We used a technique called **Simulation-Based Calibration (SBC)**. This involves:
        *   Creating many thousands of "synthetic subjects" where we *know* their true NES parameter values.
        *   Simulating how these synthetic subjects would behave in a decision task.
        *   Then, using advanced statistical methods (Neural Posterior Estimation - NPE, a form of AI/machine learning) to try and recover the original "true" parameters from the simulated behavior.
    *   **Outcome:** After much iteration and debugging (a "misery mire" at times!), we successfully showed that our pipeline *could* reliably recover all the core NES parameters from simulated data, given a well-designed task. This was a huge technical win, giving us confidence in our fitting methods.

2.  **The Acid Test - Real Human Data (The Roberts et al. Framing Study):**
    *   With a validated fitting procedure, we moved to test NES against real human behavior. We used data from a published study by Roberts and colleagues (2022) on **framing effects**. Framing effects occur when people make different choices based on whether options are presented as gains (e.g., "keep $10") or losses (e.g., "lose $0 from $10"), even if the objective outcomes are the same. This is a classic case where "normative" considerations (like loss aversion) seem to play a role. The study also included a **time pressure** condition, which often amplifies framing effects.
    *   **Our Hypothesis:** `v_norm` in our NES model should capture individual differences in how susceptible people are to these framing manipulations.

3.  **Initial Fitting and a Puzzle (The 4-Parameter Model):**
    *   We fitted the basic 4-parameter NES model (`v_norm`, `a_0`, `w_s_eff`, `t_0`) to each of the 45 human participants.
    *   **The Puzzle:** While we could estimate `v_norm` for each person, its direct correlation with their observed behavioral framing effect was weak and sometimes even in the wrong direction!
    *   **However, Posterior Predictive Checks (PPCs)** – where we used the fitted model to simulate data and see if it looked like the *real* human data – showed something interesting. The model was partially capturing the overall framing patterns (especially the amplification under time pressure) but systematically failed in specific ways: it predicted people would be much *slower* to choose "sure gains" than they actually were.

4.  **A Key Insight and Model Refinement (The 5-Parameter Model):**
    *   The discrepancy with "sure gain" RTs led to a crucial insight, guided by our advisor: humans often treat "sure gains" as obvious and decide quickly, perhaps by needing less evidence. Standard DDMs don't always account for such context-dependent threshold changes.
    *   **The Fix:** We introduced a fifth parameter to NES, called **`alpha_gain`**. This parameter specifically allows the decision threshold (`a_0`) to be *lower* (multiplied by `alpha_gain`, where `alpha_gain` is expected to be < 1, e.g., ~0.75) only for Gain-framed trials. This formalizes the idea that "when it's a sure gain, people need less evidence to commit."
    *   We re-ran the rigorous SBC process for this new 5-parameter model and confirmed that **all five parameters were now well-calibrated and recoverable.**

**Where We Are Now: Success and New Discoveries!**

We have just completed fitting this refined **5-parameter NES model** to the Roberts et al. empirical data. The results are very exciting:

1.  **`v_norm` is Validated:** With `alpha_gain` accounting for the gain-frame decision speed, `v_norm` now shows a **strong, positive, and statistically significant correlation (r ≈ 0.87) with the overall behavioral framing effect.** This means individuals our model estimates as having a higher "norm weight" are indeed more susceptible to framing manipulations in their choices. This is a core success.
2.  **`alpha_gain` is Meaningful:** The estimated `alpha_gain` values are generally less than 1 (as expected) and vary across individuals. This parameter correlates with how quickly people respond in gain frames, particularly under time pressure. This suggests it's capturing real individual differences in how decision caution is adjusted for "easy" gain choices.
3.  **Disentangling Effects:** We've successfully disentangled a general normative influence (`v_norm`) from a context-specific adjustment in decision caution (`alpha_gain`).

**So What? The Significance of These Findings:**

*   **A Mechanistic Account of Normative Influence:** NES provides a process-level model of how abstract norms can integrate with other information during decision-making, going beyond just describing *that* framing happens to explaining *how* it might unfold over time.
*   **Understanding Time Pressure:** The model offers insights into why framing effects are amplified under time pressure – not just as a black box, but through the truncation of an evidence accumulation process where early normative or salient influences can become decisive.
*   **Quantifying Individual Differences:** Parameters like `v_norm` and `alpha_gain` offer new ways to quantify individual differences in normative susceptibility and decision style, which could be linked to personality or other cognitive traits in future research.
*   **A Step Towards a More "Human" AI:** While this is cognitive modeling, the principles of integrating normative considerations into decision architectures have implications for developing AI systems that can make more aligned and context-aware choices.

**Next Steps:**

Our immediate next step is to conduct detailed **Posterior Predictive Checks (PPCs)** for this successful 5-parameter model fit. We need to ensure that it not only produces sensible parameter correlations but can also *generatively reproduce* the detailed patterns of choices and response times observed in the human data across all experimental conditions. This will be the final confirmation of its descriptive and explanatory power for this dataset.

This journey, from theoretical conceptualization through rigorous validation and now to insightful empirical application, showcases the power of computational modeling to dissect complex human cognition. We're excited by these results and the new avenues for research they open up.

---