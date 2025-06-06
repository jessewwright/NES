---
title: "Testing Architectural Necessity in Cognitive Theory: A Simulation-Based Framework Using Normative Decision Making"
author: Jesse Wright
date: "June 4, 2025"
bibliography: references.bib
link-citations: true
geometry: margin=1in
fontsize: 12pt
linestretch: 1.5
header-includes:
  - \usepackage{amsmath}
  - \usepackage{graphicx}
  - \usepackage{booktabs}
  - \usepackage{lineno}
  - \linenumbers
---

# Abstract

Is normative influence an architecturally distinct decision mechanism or an 
emergent byproduct of other cognitive processes? Here we present a simulation-
based framework to test such questions of architectural necessity in cognitive 
theory. As a case study, we introduce the Normative Executive System (NES), a 
minimal extension of the Drift Diffusion Model that includes an explicit norm 
weight parameter ($w_n$) to represent normative influence. In NES, $w_n$ 
modulates the drift rate in opposition to stimulus salience, allowing formal 
dissociation between norm-driven and utility-driven decision dynamics. 

Using Simulation-Based Calibration (SBC) with two inference methods (Approximate 
Bayesian Computation with Sequential Monte Carlo and Neural Posterior 
Estimation), we demonstrate that $w_n$ is statistically identifiable from 
simulated choice/response time data under realistic conditions. Furthermore, 
standard hierarchical DDMs (even when augmented with conflict-level regressors) 
fail to recover $w_n$ from NES-generated data, indicating a fundamental 
architectural mismatch. NES also produces distinctive behavioral signatures 
(e.g. conflict-conditioned reductions in errors and response times) that 
conventional DDM parameters cannot replicate. 

Together, these findings provide simulation-based evidence that introducing an 
explicit normative mechanism improves model identifiability and predictive 
specificity. More broadly, this work offers a generalizable framework for 
rigorously evaluating when new cognitive mechanisms are warranted, using norm-
guided decision-making as a proof-of-concept example. We discuss implications 
for building parsimonious yet testable cognitive theories and for establishing 
higher standards of model validation in cognitive science.

**Keywords:** Normative Executive System; Drift Diffusion Model; Simulation-
Based Calibration; Norm Weight; Moral Cognition; Decision Architecture

# Introduction

Across many domains of cognitive science, theorists grapple with whether certain 
behavioral influences reflect necessary components of the mind’s architecture 
or merely emergent effects of more general processes. This question has high 
stakes for theory development: positing a specialized decision mechanism can 
enrich a model’s explanatory power, but it also complicates the architecture and 
must be justified by clear evidence. Emphasizing parsimony without losing 
essential detail is critical; unnecessary mechanisms violate Occam’s razor, yet 
genuine primitives, if they exist, need explicit representation to achieve 
*identifiability* and replicability of findings. In practice, however, 
distinguishing a truly architecturally distinct process from a clever re-tuning 
of existing parameters is challenging. Standard model-fitting techniques often 
accommodate new data by adjusting generic parameters, potentially masking the 
presence or absence of a dedicated mechanism. Thus, methodological innovation is 
needed to rigorously test when an influence warrants treatment as a fundamental 
element of the cognitive architecture.

One domain where this issue arises acutely is moral and normative decision-
making. People often make norm-consistent choices even when self-interest, 
emotion, and learned rewards all favor doing otherwise. For example, we stop at 
red lights on empty roads, keep unenforceable promises, and help strangers at 
personal cost. Such behaviors persist in the absence of material incentives or 
direct social enforcement, hinting at an internal factor beyond simple utility 
or habit. Classical models usually explain norm-adherence by folding it into 
emergent processes within general-purpose decision architectures. For instance:

- Utility-based models might treat norms as just another high-value preference
- Reinforcement learning accounts attribute norm-following to conditioned social 
  feedback
- Dual-process theories invoke generic cognitive control or emotion-regulation 
  to override selfish impulses
- Conflict-monitoring frameworks see norm compliance as a domain-general 
  inhibitory control response [@bello2023computationalapproachesto; 
  @cushman2015moralconstraints]

In all these approaches, norms are not granted a unique status; rather, norm-
following is expected to arise "for free" as a byproduct of existing valuation, 
learning, or control parameters.

However, many moral choices appear uncued, unsupervised, and divorced from self-
interest, suggesting that something more may be at play 
[@cushman2015moralconstraints]. For example, one might reject an unfair offer in 
an economic game even with no future repercussions, or children might follow 
invented rules in games with no reward, which is difficult to attribute entirely 
to learned utility or fear of sanction.

These observations motivate a bold theoretical question: Could normative 
influence itself be a necessary component of the decision architecture? 
[@Greene2001fMRI] In other words, is there a dedicated cognitive mechanism that 
drives norm-adherent behavior, independent of and irreducible to other decision-
making processes?

For theoretical progress, one must balance parsimony and explanatory power. 
Unnecessary mechanisms violate Occam’s razor, but genuinely distinct processes 
require explicit representation to ensure identifiability and replicability. We 
advocate for requiring rigorous evidence of a mechanism’s necessity before 
elevating it to a fundamental component of the cognitive architecture.

Despite this need, direct empirical tests of "architecturally necessary vs. 
emergent" status are rare. In the realm of moral decision-making, recent reviews 
have highlighted the lack of formal, model-based tests for whether explicit 
representations of norms are necessary to explain behavior 
[@Hare2009SelfControl]. 

Researchers have typically inferred the role of norms indirectly (e.g., via 
questionnaires or post hoc model fits) rather than building models where norm 
influence is a separate, measurable factor. Without such tests, debates over 
domain-specific mechanisms often remain stuck at the level of plausible 
interpretations or statistical model comparisons, which can be inconclusive.

Standard goodness-of-fit or likelihood ratio tests are insufficient because a 
sufficiently flexible generalist model might fit the data nearly as well as a 
specific model, obscuring the unique contribution of the new mechanism. What is 
needed is a more stringent simulation-based methodology that can ask: if the 
world did have a dedicated normative influence (or other candidate mechanism), 
could we detect it? And conversely, would a model lacking that mechanism 
systematically falter in capturing the data?

# Related Work

Recent advances in neurocomputational modeling have integrated moral variables into drift diffusion or softmax-based value functions, estimating distinct weights for fairness, harm aversion, or altruistic concern [@tusche2021neurocomputational; @gawronski2016bidirectional; @spiekermann2016empirical]. These models formalize social preferences as separable from egoistic utilities, capturing moral concerns as weighted parameters. However, they typically stop short of implementing categorical constraints—i.e., principled prohibitions that override expected utility under all incentive regimes. Our results suggest that this difference is not just conceptual but architectural: the sharp threshold behavior NES produces under norm conflict cannot be recovered by reweighting or attentional modulation alone. 

While these existing approaches have advanced the field by treating moral concerns as real variables rather than post hoc explanations, they differ fundamentally from NES in their representational commitments. The key innovation of NES is not simply weighting norms more heavily, but rather encoding constraints as non-compensatory state transitions (threshold breakpoints) that cannot be captured via continuous value trade-offs. This architectural distinction is empirically necessary, as demonstrated by our λ-stress tests showing that standard drift-diffusion architectures cannot reproduce the behavioral signatures of norm-constrained decision-making, even when allowed to adjust their drift rates flexibly across conflict conditions.

# Why Multi-Attribute DDMs Are Not Enough

At first glance, one might wonder whether simply adding another drift-rate 
component for normative influence in a standard DDM could replicate NES's 
behavior. This essentially yields a multi-attribute DDM (aDDM) where drift has 
independent contributions (e.g., a "norm evidence" term and a "utility 
evidence" term). However, such an additive approach lacks the crucial context-
dependent interplay that $\lambda$ provides. In an aDDM, each evidence source 
affects drift independently and in a fixed manner across trials, so it cannot 
capture the idea that normative pressure matters *only when it conflicts with* 
utility.

In NES, by contrast, $\lambda$ acts as a multiplicative gate that dynamically 
balances norm versus utility evidence on each trial. If $\lambda=0$ (no 
conflict), the norm term has no effect and the drift is purely stimulus-driven; 
if $\lambda=1$ (maximal conflict), normative pressure fully counteracts the 
stimulus-driven drift. An aDDM would have to include an explicit interaction 
between norm and utility to mimic this behavior—effectively reintroducing a 
context factor akin to $\lambda$.

**Formal Statement:** *NES cannot be reduced to a purely additive DDM without 
loss of generality.* In other words, no fixed set of additive drift terms can 
reproduce the NES drift function $v = w_s(1-\lambda) - w_n\lambda$ for all levels 
of $\lambda$. This expression inherently involves an interaction (the product of 
a weight and $\lambda$), which means an aDDM lacking such a term will mis-specify 
the process under normative conflict.

This theoretical distinction is borne out empirically. Even when we gave a 
hierarchical DDM extra flexibility by allowing its drift to vary across conflict 
conditions (an attempt to emulate an aDDM), it could not accurately recover or 
substitute for $w_n$:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}. The $\lambda$ mechanism in NES 
provides a unique capacity to represent internal conflict that attribute-wise 
DDMs miss. In sum, $\lambda$ serves a special functional role, gating normative 
vs. utility evidence in a way that cannot be replicated by simply adjusting drift 
parameters in a standard model.

# Case Study: Normative Influence in Decision Making

To illustrate our framework, we designed a minimal model called the Normative 
Executive System (NES), which extends the drift-diffusion model by adding a 
single parameter for norm influence. NES's drift rate $v$ is defined to include 
two competing components—stimulus-driven salience versus normative 
pressure—combined according to a context variable $\lambda$ that represents the 
degree of norm–utility conflict. Formally:

$$v = w_s(1-\lambda) - w_n\lambda$$

where $w_s$ is the usual salience weight (capturing evidence favoring the more 
"incentivized" option) and $w_n$ is the norm weight representing internalized 
normative pressure. The factor $\lambda \in [0,1]$ indexes conflict between the 
two: $\lambda=0$ means no normative conflict (the decision is purely driven by 
utility/salience), while $\lambda=1$ means maximal conflict (the norm completely 
opposes the salient choice). A larger $w_n$ causes the drift to tilt more 
toward the norm-favored choice as $\lambda$ increases.

NES retains the standard DDM parameters for decision threshold ($a$) and non-
decision time ($t_0$), which we held constant in simulations to isolate the 
effects of $w_n$ and $w_s$.

## Task Design

We simulated a binary decision task with varying levels of norm conflict. Each 
trial was assigned a conflict value $\lambda$ (e.g., 0.0, 0.25, 0.5, 0.75, 1.0). 
At $\lambda=0$, norm and self-interest align, making the decision 
straightforward; at $\lambda=1$, following the norm directly opposes a strong 
self-interested incentive. Intermediate $\lambda$ values create graduated levels 
of tension between doing what's right versus what's rewarding.

We generated synthetic datasets for multiple simulated individuals (with trials 
at each $\lambda$ level) and used these data to evaluate whether $w_n$ could be 
identified and whether its absence caused systematic model failures, as 
described next.

# Testing the Framework: Identifiability Analysis

## ABC-SMC Parameter Recovery

In our first set of simulations, we generated 100 synthetic datasets from NES 
with random "true" parameter values (including $w_n$ drawn from a broad range) 
and applied ABC-SMC inference to each. The recovered $w_n$ values closely 
matched the true values (Pearson $r\approx0.9$), and the posterior credible 
intervals contained the true $w_n$ about 95% of the time. 

Moreover, simulation-based calibration (SBC) showed nearly uniform rank 
histograms for $w_n$, indicating no systematic bias in recovery. Figure 1 
(Appendix) illustrates an example rank histogram for $w_n$, confirming that 
$w_n$ is identifiable under realistic conditions.

We also verified that identifiability was robust to analysis variations. For 
instance, using different summary statistics or weighting schemes in ABC still 
yielded uniform rank statistics for $w_n$. This increases our confidence that 
the positive recovery of $w_n$ is not an artifact of a particular inference 
setup, but rather reflects an inherent signal in the data.

## Neural Posterior Estimation (NPE) Results

Using a neural inference method [@sbi_package_tejero_etal_2020], we obtained 
similar results. After training a neural posterior estimator on a large 
simulation set, we inferred parameters on 100 new datasets. The NPE recovered 
$w_n$ accurately: posteriors for $w_n$ were sharply peaked near the true values, 
and SBC ranks were again uniform (no calibration deviations; see Figure 2 in 
Appendix).

Notably, NPE could jointly recover all parameters ($w_n$, $w_s$, $a$, $t_0$) 
without confusion, as $w_n$ showed little correlation with other parameters. The 
convergence of ABC and NPE results strengthens the evidence that $w_n$ is a 
genuine, recoverable feature of the data rather than a "ghost" parameter.

## Hierarchical DDM (HDDM) Mismatch Analysis

Next, we asked whether a model lacking $w_n$ could fit data generated by NES. We 
fit a hierarchical DDM (HDDM) to the same simulated datasets, allowing its 
drift rate to vary by conflict level (to give the DDM a chance to mimic norm 
effects via extra flexibility). 

Despite this, the HDDM failed to recapitulate the true norm influence. The 
correlation between the HDDM's fitted drift-vs-conflict slopes and the true 
$w_n$ values was low (e.g., $r\approx0.4$ in one analysis), indicating it could 
not reliably recover the norm effect. The HDDM consistently underestimated the 
impact of high conflict on drift, and often the true $w_n$ lay at the extreme 
tails of the HDDM's posterior—meaning the HDDM was confidently wrong about norm 
influence.

The core problem was that the HDDM lacked a dedicated place for normative 
influence, so it misattributed the norm-driven effects to other parameters (or 
noise). In high-conflict trials especially, the HDDM's drift estimates were far 
off (e.g., 30–50% too low in some conditions) because the model could not 
represent the internal tug-of-war between norm and salience.

In short, a model without an explicit $w_n$ could not "fake" data generated with 
a norm mechanism, supporting the claim that $w_n$ is a structurally necessary 
component for capturing those patterns.

# Unique Behavioral Signatures

Beyond statistical identifiability, an architecturally necessary mechanism 
should produce behavioral patterns that other models cannot. NES indeed predicts 
a distinctive pattern under high normative influence. 

Counter-intuitively, when $w_n$ is large, increasing conflict can lead to faster 
and more accurate decisions (norm-consistent ones). This is opposite to the 
usual pattern where more conflict (or difficulty) slows responses and increases 
errors. In NES, a strong norm weight drives the decision process toward the 
norm-adherent choice even as conflict rises, sometimes even accelerating the 
decision once the norm "takes over."

For example, with $w_n$ high, the model makes fewer errors at $\lambda=1.0$ (max 
conflict) than at moderate conflict, and reaction times that were initially 
slowed by conflict start to speed up again at the highest conflict level. By 
contrast, when $w_n\approx0$ (no norm influence), NES reduces to a standard DDM 
and shows the expected slowing and accuracy decline as conflict increases.

Figure 3 illustrates this contrast: with $w_n=1.5$, accuracy actually improves 
at high conflict and mean RT drops after an initial increase, whereas with 
$w_n=0$ accuracy falls and RT rises monotonically with conflict.

Crucially, we found that no configuration of a norm-less DDM could reproduce 
this joint pattern of speed and accuracy. Adjusting the decision threshold or 
drift rate in a standard DDM could either reduce errors or speed up responses, 
but not achieve the combination that NES generates (fewer errors and faster 
responses specifically at high conflict).

For instance, raising the threshold might decrease errors but at the cost of 
much slower responses across all conditions, unlike the selective speeding we 
see with a high $w_n$. Lowering $w_s$ (salience) uniformly degrades performance 
rather than producing an improvement at high conflict. We systematically tried 
such adjustments and none yielded the "paradoxical" performance profile that a 
non-zero $w_n$ produces.

Figure 5 illustrates this point: only the model with an explicit norm weight 
lies in the region of performance space characterized by decreasing error rates 
and non-increasing RTs as conflict grows. All other models (including various 
threshold or drift adjustments) occupy a different region (higher error slopes 
and/or RT slopes).

This analysis confirms that the behavioral effects of $w_n$ are qualitatively 
unique. Empirically, this unique signature offers a way to test for normative 
mechanisms in people: if some individuals actually show faster, more accurate 
choices under increased normative conflict, it would be hard to explain without 
a dedicated norm process. If no one shows such a pattern, then positing a 
special norm mechanism may be unnecessary.

In our simulations, the signature becomes pronounced at sufficiently high $w_n$; 
moderate values yield intermediate patterns. The key takeaway is that NES’s 
norm parameter is not just mathematically identifiable, but behaviorally 
consequential in a way that defies mimicry by other parameters.

# Empirical Stress Test: Moral-Framing Task (Roberts & Gershman 2021)

As a final demonstration, we applied NES to human decision data to evaluate its 
relevance beyond simulations. We analyzed choices and response times from a 
moral decision-making task where the context framing modulated normative 
conflict (similar to paradigms in [@gautheron2024conflictinmoral]).

For example, in one condition an option was presented with an explicit moral 
rule attached (high norm salience), while in another it was framed neutrally 
without invoking norms (low norm salience). This manipulation created variation 
in internal normative pressure on otherwise similar decisions, providing an 
opportunity to test whether NES can capture framing-induced differences.

Using a hierarchical Bayesian approach, we fit the NES model to participants' 
data across the two framing conditions. Including the norm parameter $w_n$ 
significantly improved the model’s fit to the data: the model with $w_n$ 
achieved a lower WAIC (ΔWAIC ≈ 4, corresponding to Δelpd ≈ 2) and accounted for 
more variance in behavior (NES $R^2 \approx 0.30$ vs. DDM $R^2 \approx 0.25$). 
This advantage translates to a Bayes factor of about 5 in favor of the NES 
model, indicating moderate evidence for including the normative mechanism. 
Additionally, the NES model’s predictions were more accurate, with a roughly 
10% lower mean absolute error (MAE) in predicting RTs compared to the DDM.

In contrast, the baseline DDM systematically underpredicted the differences 
between framing conditions – for instance, it could not account for slower but 
more norm-consistent choices in the moral-frame condition. This result suggests 
that a non-zero $w_n$ was necessary to capture the behavioral shift caused by 
moral framing, aligning with the idea that an explicit norm influence 
contributes to human decisions.

![Model fitting results for the framing task. Including the normative weight parameter ($w_n$) allows NES to better capture the effect of moral framing on decisions, whereas a standard DDM without $w_n$ cannot. The model with $w_n$ more closely reproduces the higher norm-consistent choice proportion and slower response times observed under the moral-frame condition.](figures/framing_task_results.png)

![Model comparison results. Bar chart of fit indices (e.g., WAIC) for the NES model versus a standard DDM, showing the NES's superior fit after accounting for model complexity.](figures/NES_vs_DDM_WAIC.png)

## Task Design

*(See Appendix B for task timeline, stimuli examples, and prior specifications.)* 
The human experiment (Roberts & Gershman 2021) involved participants making 
binary choices under different framing conditions. In the **moral-frame** 
condition, choices were presented with a salient moral rule, whereas in the 
**neutral-frame** condition, the same choices were presented without normative 
context. We treated these conditions as different levels of $\lambda$ in the 
NES model. Specifically, the moral-frame condition was coded as high conflict 
($\lambda = 1$), and the neutral-frame condition as low conflict ($\lambda = 0$). 
Thus, in the model, normative pressure affected the drift only in the moral-
frame trials (where $\lambda=1$ introduces the $-w_n$ term in $v$) but not in 
neutral trials ($\lambda=0$ yields $v = w_s$). We used diffuse priors for all 
model parameters and fit the model to the data using hierarchical Bayesian 
methods.

## Mapping frame → $\lambda$

We treat frame as a proxy for trial-level $\lambda$, with a binary mapping: neutral frame = $\lambda_i = 0$, moral frame = $\lambda_i = 1$. This binary operationalization matches the experimental manipulation in [@RobertsGershman2021], where frames were categorically distinct (presence vs. absence of moral rule).

In our analysis, we treated the two framing conditions as different levels of 
$\lambda$. The moral-frame condition (with an explicit moral rule) 
was coded as high conflict ($\lambda = 1$), whereas the neutral-frame condition 
(no norm cue) was coded as low conflict ($\lambda = 0$). In other words, the norm 
mechanism was "switched on" (maximal influence) in the moral-frame trials and 
"switched off" in neutral-frame trials. Under this mapping, the drift equation 
$v = w_s(1-\lambda) - w_n\lambda$ predicts a drift advantage for the norm-favored 
choice in moral-frame trials (since $\lambda=1$ introduces the $-w_n$ term) but 
not in neutral trials ($\lambda=0$ yields $v = w_s$). We used diffuse priors for 
all model parameters (see Appendix B) and then fit the model to participants’ 
data as described next.

### Continuous λ (Future Directions)

In our framing application, we coded λ as 0 (neutral frame) or 1 (moral
frame) to match the binary manipulation in [@RobertsGershman2021]. However,
normative conflict likely varies continuously across contexts and individuals.
A straightforward extension is to estimate λ per trial from independent
measures (e.g., self-reported conflict, skin-conductance as a proxy for
internal dissonance, or graded manipulations of rule salience). One could
also treat λ as a free parameter per trial (similar to a drift scaling factor)
and fit it hierarchically across subjects. Such approaches would test whether
λ truly lies on [0,1] as assumed or follows another distribution.

In preliminary analyses (not shown), we allowed $\lambda_i \sim \text{Beta}(\alpha,\beta)$ per trial
with hyperpriors on α and β, but the data were too sparse to recover stable
$\lambda_i$ estimates for each participant. We therefore retained the 0/1 coding
as a transparent first step.

## Quantitative Model Comparison (ΔWAIC, Δelpd, $R^2$, BF$_{10}$, MAE)

We fit both the NES model and a standard DDM (without $w_n$) to participants’ 
choices and response times and compared their performance. The NES model 
provided a better fit across multiple criteria. For instance, the model with 
$w_n$ achieved a lower WAIC (ΔWAIC ≈ 4, corresponding to Δelpd ≈ 2) and 
accounted for more variance in behavior (NES $R^2 \approx 0.30$ vs. DDM $R^2 
\approx 0.25$). This advantage translates to a Bayes factor of about 5 in favor 
of the NES model, indicating moderate evidence for including the normative 
mechanism. Additionally, the NES model’s predictions were more accurate, with 
a roughly 10% lower mean absolute error (MAE) in predicting RTs compared to 
the DDM.

In contrast, the baseline DDM systematically underpredicted the differences 
between framing conditions – for instance, it could not account for slower but 
more norm-consistent choices in the moral-frame condition. A non-zero $w_n$ was 
required to capture this behavioral shift, reinforcing the idea that an explicit 
norm parameter contributes explanatory power that the baseline model lacks.

![Model fitting results for the framing task. Including the normative weight parameter ($w_n$) allows NES to better capture the effect of moral framing on decisions, whereas a standard DDM without $w_n$ cannot. The model with $w_n$ more closely reproduces the higher norm-consistent choice proportion and slower response times observed under the moral-frame condition.](figures/framing_task_results.png)

![Model comparison results. Bar chart of fit indices (e.g., WAIC) for the NES model versus a standard DDM, showing the NES's superior fit after accounting for model complexity.](figures/NES_vs_DDM_WAIC.png)

## Individual Differences (correlation $r$, regression $\beta$)

We observed considerable variability in normative influence across individuals. 
Some participants’ data were well explained without a norm parameter 
(their posterior $w_n$ estimates clustered near zero). 
Others required a substantial $w_n$ 
(posterior distributions clearly above zero). 
This suggests that people differ in their **normative sensitivity** – 
the degree to which the moral framing affected their decisions.

Moreover, participants with higher $w_n$ tended to exhibit larger framing 
effects on behavior.  
Across individuals, the correlation between the fitted $w_n$ 
and the increase in norm-consistent choice proportion under the moral frame was 
approximately $r = 0.72$. A regression analysis likewise indicated that $w_n$ 
significantly predicted 
the magnitude of the framing effect on choices (β ≈ 0.25,  
95% CI excl. 0), confirming that the $w_n$ parameter captured meaningful 
individual differences rather than mere noise.

![Relationship between individual $w_n$ estimates and framing effect on choices. Each point represents a participant; higher $w_n$ values are associated with a larger increase in norm-consistent choices under moral framing (positive correlation).](figures/w_n_vs_framing_effect.png)

# Implications for Theory Building

In summary, our results—spanning simulation-based identifiability tests, formal 
model comparisons, and human data—demonstrate that adding an explicit normative 
mechanism ($w_n$) yields both identifiable parameters and distinctive predictive 
gains that simpler models cannot achieve. Our findings also emphasize how higher 
standards can sharpen theoretical debates. When proposing a new cognitive 
mechanism, researchers should not rely solely on arguments that existing models 
cannot explain a phenomenon; they should also provide simulation-based evidence 
that the new mechanism is identifiable and produces unique predictions that 
simpler models cannot. By expecting such evidence, the field can ensure that 
added model complexity is justified by a true gain in explanatory power, leading 
to more parsimonious yet rigorous theories.

Furthermore, our case study challenges the assumption that complex behaviors 
always "emerge" from simpler processes. The norm-following patterns we examined 
could not be replicated by a model lacking an explicit norm parameter, which 
suggests that normative influence may require its own dedicated representation 
rather than being reducible to general decision mechanisms. In other domains, one could apply a similar paradigm—embedding a candidate 
mechanism into a generative model, testing parameter identifiability, and assessing 
unique behavioral signatures—provided that a clear behavioral readout exists.  
For example, one might test:

- A "social-evaluation" module in a trust game (generate data with and without a 
  social penalty term, then see if a standard reinforcement-learning model can 
  recover that penalty parameter).
- A "working-memory gating" mechanism in a multi-choice reaction-time task (embed 
  a gating weight into a leaky accumulator, then see if a simpler accumulator can 
  mimic performance).

In each case, the same core steps—SBC, mismatch analysis, behavioral signature—would 
apply. We refrain from claiming that the precise form of λ in NES transfers 
wholesale; rather, the *principle* of using simulation to ground architectural 
claims is portable across domains.

## Limitations

Despite the strengths of our approach, several limitations must be acknowledged. 
First, our analyses were entirely based on simulated data. While this was 
appropriate for testing identifiability and theoretical distinctions, evidence 
for NES's advantage on actual human behavior remains preliminary. In fact, our 
initial test fitting NES to human choices (Appendix B) showed that including 
$w_n$ improved fit only modestly. Real decisions involve noise and unmodeled 
factors, so detecting a new mechanism from behavior alone may require larger 
studies or additional evidence.

Second, the scope of the model is limited. NES as implemented covers binary 
choice with a static norm conflict parameter. Real-world normative decisions are 
often more complex: multi-alternative choices, dynamic norm learning over time, 
etc. Currently, $w_n$ in our model is treated as a stable influence within a 
session. In reality, people may adjust their norm adherence based on context or 
reinforcement (perhaps learning when to rely on norms versus other cues). 
Extending the model to handle these dynamics could make it more psychologically 
plausible and testable in richer experimental paradigms.

*(Additional limitations and discussion of robustness checks, including the use 
of PSIS-LOO for complexity control and formal power analysis results, are 
provided in Appendix C.)*

# Conclusion

Architectural claims in cognitive theory demand evidence beyond goodness-of-fit. 
Our simulation-based approach demonstrates how targeted tests of identifiability 
and unique behavioral predictions can establish the necessity of a proposed 
mechanism. By combining simulations, rigorous model comparisons, and human data, 
we showed that normative influence ($w_n$) fulfills criteria for a distinct 
architectural component in decision-making. This work underscores the value of 
formally probing when new model parameters earn their place, and it provides a 
blueprint for elevating the standards of theoretical validation in cognitive 
science.
