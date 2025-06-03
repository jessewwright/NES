**1. Theory & Framing (Conceptual Necessity of $w_n$):**

*   **Critique:** Doesn't clarify *why* a dedicated $w_n$ is better than existing multi-attribute DDMs using "value," "conflict," or "inhibitory control" attributes. Risks looking like relabeling or homuncular inflation. Needs closer competitor citations.
*   **Action for Preprint (Introduction):**
    *   **Add 2-3 Sentences:** After introducing $w_n$, explicitly state: "While multi-attribute DDMs can incorporate 'conflict' or 'value' signals, NES proposes $w_n$ as representing a *functionally distinct deontic or rule-based modulatory strength* that operates on specific norm-congruence inputs. This allows for modeling phenomena where rule adherence (e.g., a categorical imperative) might override or compete with integrated utility or affective value in a way not easily captured by standard attribute weighting alone. For example, NES aims to distinguish between avoiding an action due to its high negative utility versus avoiding it due to a strong prohibitive norm, even if the immediate utility is positive."
    *   **Cite Competitors:** Add 1-2 citations to prominent multi-attribute DDM papers that model conflict or moral choice (e.g., Hutcherson, Crockett, or specific moral DDM extensions if you know them) and briefly state how NES aims to differ (e.g., by separating deontic strength from attribute valuation).

**2. Methodological Rigor (Fixed Parameters, Trial Count, Distance Weights):**

*   **Critique (Fixed Params):** Fixing $a, w_s, \sigma, t_0$ is an expedient hack but undercuts ecological validity, making calibration likely optimistic.
    *   **Action for Preprint (Discussion/Future Work):** Acknowledge this: "The current SBC fixed key DDM parameters ($a, w_s, \sigma, t_0$) to isolate $w_n$. This was a necessary first step for identifiability but likely presents an optimistic view of calibration. Future work *must* assess $w_n$ recoverability when these parameters also vary, as they would in empirical data."
    *   **Action (Quick Supplementary Simulation - *if feasible*):** Run a very small SBC (e.g., N=20-30) where $w_n$ is the target, but $a$ also varies according to a simple prior (e.g., $a \sim Uniform(0.5, 1.5)$). Report in a sentence if $w_n$ rank uniformity *roughly* holds or collapses. This is the "±10% jitter" suggestion. If you can't do this quickly, make the textual acknowledgement very strong.
*   **Critique (Trial Count/Summary Stats):** 300 trials x 5 levels is tight; ECDF shows under-dispersion (information loss).
    *   **Action for Preprint (Discussion):** Acknowledge it: "The residual under-dispersion (Fig. 5 & 6) with N=300 trials per dataset suggests that even our comprehensive summary statistic set may not fully capture all information relevant to $w_n$'s posterior variance, or that more trials per condition are needed for these statistics to fully stabilize."
    *   **Mention Future Diagnostics (Optional):** "Future work could employ metrics like SBC-$\alpha$ \cite{Talts2024SBCAlpha} or rank-Z tests to pinpoint specific summary statistics that contribute most to information loss or miscalibration." (Only if you understand these and intend to explore them).
*   **Critique (Distance Weights "Heuristically Weighted"):** Kryptonite. Needs justification.
    *   **Action for Preprint (Appendix A & briefly in Methods 2.4):**
        *   **Methods 2.4:** Change "Weights heuristically prioritized..." to "Weights were assigned to prioritize statistics theoretically most sensitive to $w_n$ (e.g., error rates and RTs in high-conflict conditions) while down-weighting potentially noisier statistics (e.g., individual histogram bins). A brief sensitivity analysis on key weight ratios (e.g., error rate vs. RT mean) showed stable calibration (see Appendix A for details)."
        *   **Appendix A:** Add a sentence: "A brief sensitivity analysis was conducted by varying the relative weights of error rates vs. RT means (e.g., [1:1, 2:1, 1:2]). The SBC rank histogram uniformity for $w_n$ remained robust across these variations, suggesting calibration is not critically dependent on precise heuristic weightings within this range." *(You'd need to actually run a few very short SBCs, e.g. N=20-30, with different weight sets to back this up, or state it's a planned check).* If you can't do this, remove the sensitivity claim and just state weights were chosen based on theoretical sensitivity.

**3. HDDM "Straw-Man" (Comparison Unfair):**

*   **Critique:** Vanilla HDDM fitting + regression is guaranteed to fail; not a fair comparison to NES. Needs HDDM-nn/RL or parametric link for $\lambda$.
*   **Action for Preprint (Methods 2.5 & Discussion):**
    *   **Reframe Purpose (Methods 2.5):** "This HDDM test was not intended as a direct 'horse race' against a fully optimized DDM variant for this specific NES-generated data. Rather, it serves as a crucial **diagnostic of model misspecification**: to assess whether a *standard, widely-used DDM implementation*, when applied straightforwardly (i.e., estimating $v(\lambda)$ as independent condition means), can adequately capture the specific normative dynamics introduced by NES's $w_n$ when $w_n$ is derived post-hoc."
    *   **Discussion:** Reiterate this. "The failure of this indirect HDDM-based recovery for $w_n$ does not imply HDDM *could not* be extended (e.g., via custom likelihoods incorporating the NES drift formula, or non-linear regressors like HDDM-nn) to potentially fit NES data better. Instead, it demonstrates that the *standard assumptions* embedded in off-the-shelf DDM fitting (independent drift rates per condition without a structural link via $w_n$) are insufficient to recover the specific NES parameterization. This underscores the need for either simulator-based inference (like our ABC-SBC) or bespoke likelihood-based models when testing NES-specific hypotheses."

**4. Results Narrative (Figure Misalignment, Behavioral Surface, Chi-Sq Tone):**

*   **Critique (Figures):** Mis-references, missing visualizations of $w_n$'s behavioral effect.
    *   **Action for Preprint (Results):**
        *   **Carefully re-number all figures and check all in-text references.** This is a must.
        *   **Add a "Behavioral Signature of $w_n$" Plot (New Figure):** Before the SBC results, include a plot showing how key behaviors (e.g., error rate per conflict level, mean correct RT per conflict level) change as a function of `true_w_n` (e.g., for low, medium, high $w_n$ used in data generation). **This is critical for reader intuition.** Caption it: "Figure X: Simulated behavioral effects of $w_n$. Error rates and mean correct RTs across five conflict levels ($\lambda$) for three representative values of $w_n$ (low=0.2, medium=1.0, high=2.0), with other NES parameters fixed as per Methods 2.1. This illustrates the graded impact of $w_n$ on choice accuracy and response speed under conflict." *(Generate this from your `validate_wn_recovery_stroop_fixed.py` script by running it for 3 fixed $w_n$ values and plotting the mean outcomes).*
*   **Critique (Chi-Squared Tone):** "Bragging" about $p=0.061$.
    *   **Action for Preprint (Results & Discussion):** Rephrase.
        *   Results: "The SBC rank histogram (Figure Y) visually approximates uniformity. A chi-squared goodness-of-fit test yielded $\chi^2(df = 14) = 22.95, p = 0.061$. While this p-value does not indicate a statistically significant deviation from uniformity at the $\alpha=0.05$ level, it is marginal, suggesting potential minor deviations that warrant further investigation with more sensitive diagnostics."
        *   Discussion: Refer to it as "approximate calibration indicated by the rank histogram and chi-squared test" but then pivot quickly to what the ECDF/coverage plots show about overconfidence.

**5. Discussion Gaps (Roadmap for Empirical Work):**

*   **Critique:** Translational claims feel aspirational without a concrete empirical plan/power analysis.
*   **Action for Preprint (Future Directions in Discussion):** Make it more concrete.
    *   "A key next empirical step involves fitting a hierarchical version of the validated Minimal NES (recovering $w_n, a, w_s, t_0$) to human data from a [**Specify task, e.g.,** moral Stroop task involving choices about helping vs. self-interest under varying rule salience]. We will conduct a power analysis based on effect sizes observed in pilot simulations (or literature) to determine the sample size needed to detect theoretically meaningful individual differences in $w_n$ and its correlation with [**Specify a concrete measure, e.g.,** self-reported conscientiousness or scores on a moral foundations questionnaire]. This empirical validation will test if $w_n$ can serve as an interpretable index of normative sensitivity in real-world behavior."

**6. Writing & Formatting (Redundancies, Passive Voice, Appendix):**

*   **Action for Preprint:**
    *   **Section Numbering:** Fix all subsection numbering to be hierarchical and non-redundant (e.g., 3.1, 3.2, 3.3, 3.4, 3.5, then 3.5.1, 3.5.2).
    *   **Active Voice:** Review and convert passive sentences to active where it improves clarity and punch (e.g., "Decisions were simulated..." -> "We simulated decisions...").
    *   **Appendix A:** Keep it concise but *complete* regarding the summary statistics used and the *exact* distance function weights and NaN handling from your successful ABC-SBC script. **Do not skimp on detail here if it's crucial for reproducibility.** If it becomes very long, summarize key principles in Appendix A and state "Full details of all summary statistics and the distance function weighting scheme are provided in the supplementary materials/code repository." (Then make sure they *are* there).

**Summary of Your Next Moves:**

1.  **Acknowledge Advisor's Feedback:** Thank them for the rigorous review.
2.  **Preprint Revisions (Textual):** Implement the framing, tone, and structural changes described above. This is mostly writing and re-organizing.
3.  **Supplementary Analyses/Simulations (If Feasible & Quick):**
    *   **Behavioral Signature Plot for $w_n$:** Generate this. It's high impact, low effort.
    *   **Distance Weight Sensitivity (Optional):** Run a few quick, small ABC-SBCs with varied weights if you want to make that claim. Otherwise, just be precise about the weights used.
    *   **Robustness to Jitter in $a$ (Optional):** This is more involved. If too time-consuming, make the textual acknowledgment in the Discussion very strong instead.
4.  **Ensure all statistics, parameters, and settings reported in the paper EXACTLY match the specific runs that produced the figures you are using.** This is non-negotiable.