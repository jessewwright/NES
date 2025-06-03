# Peer Review: Validating Norm Weight Identifiability in the Normative Executive System (NES) via Simulation-Based Calibration

## Overall Assessment

This manuscript presents an interesting and technically sophisticated approach to modeling normative decision-making through the Normative Executive System (NES). The core idea—that norms constitute a functionally distinct class of decision variable—is theoretically compelling and addresses an important gap in current decision-making models. The use of Simulation-Based Calibration (SBC) to validate parameter identifiability is methodologically sound and represents good practice in computational modeling.

**Strengths:**
- Novel theoretical framework addressing an understudied aspect of decision-making
- Rigorous validation methodology using SBC
- Clear demonstration that standard approaches (HDDM) fail to capture the proposed mechanisms
- Well-structured presentation with appropriate technical detail
- Impressive technical execution for an independent researcher

**Areas for Improvement:**
- Theoretical foundations need strengthening
- Limited empirical grounding
- Some methodological choices require better justification
- Writing could be more accessible

---

## Major Comments

### 1. Theoretical Foundation and Motivation

**Strengths:**
The central thesis that norms represent a distinct computational mechanism is intriguing and potentially important. The philosophical grounding (referencing the "hegemonikon") adds conceptual depth.

**Concerns:**
- The distinction between norms and other forms of value-based decision-making needs clearer articulation. How exactly do "internalized rules or obligations" differ computationally from other learned value associations?
- The claim that traditional DDMs "rarely distinguish between utility-based and norm-based influences" may be overstated. Many existing models incorporate conflict monitoring and cognitive control mechanisms.
- More extensive review of related work is needed, particularly:
  - Conflict monitoring models (e.g., Botvinick et al.)
  - Moral decision-making models (Greene's dual-process theory)
  - Value-based decision models with multiple attributes
  - Cognitive control and executive function models

### 2. Model Specification and Validation

**Strengths:**
- The NES architecture is clearly specified
- SBC methodology is appropriate and well-executed
- The failure of HDDM to recover parameters is a compelling validation

**Concerns:**
- The drift rate equation (v = w_s⋅(1-λ) - w_n⋅λ) seems overly simplified. Why this specific functional form?
- Parameter fixing (a, w_s, t_0) for identifiability is reasonable but limits ecological validity
- The "Stroop-like" task design needs better justification—why these specific conflict levels?
- The relationship between λ (conflict level) and real-world normative conflicts needs elaboration

### 3. Empirical Grounding

**Major Limitation:**
The paper is entirely based on synthetic data. While SBC validation is important, the lack of empirical validation is a significant weakness.

**Recommendations:**
- Include at least preliminary analysis of real behavioral data
- Demonstrate that the model can account for known phenomena in moral/normative decision-making
- Show that recovered parameters correlate with meaningful individual differences

### 4. Statistical and Methodological Issues

**Generally Strong, but:**
- Some results show mild underdispersion—this needs more investigation
- The choice of summary statistics seems somewhat ad hoc
- Missing details about computational implementation
- The jitter analysis is mentioned but results are incomplete

---

## Minor Comments

### Writing and Presentation

**Positive:**
- Generally clear writing
- Good use of figures
- Appropriate level of technical detail

**Suggestions:**
- The introduction could be more accessible to readers unfamiliar with DDMs
- Some claims are overstated (e.g., "first simulation-based validation")
- Figure captions could be more informative
- Consider adding a glossary of technical terms

### Technical Details

**Missing Information:**
- Computational specifications (hardware, runtimes)
- Software versions and reproducibility information
- More details on NPE training and convergence
- Complete results from parameter jitter analysis

### Figures and Tables

**Strengths:**
- Figure 1 (NES architecture) is clear and helpful
- Behavioral signature plots (Figures 8-10) effectively demonstrate the model's predictions

**Improvements:**
- Figure quality could be enhanced (resolution, fonts)
- Some figures lack error bars or uncertainty quantification
- Table 1 formatting could be improved

---

## Specific Technical Comments

### Model Architecture
The NES framework is interesting, but the mathematical formulation could be more sophisticated. Consider:
- Non-linear interactions between norm and salience weights
- Time-varying parameters
- Individual differences in parameter relationships

### Validation Strategy
While SBC is appropriate, consider additional validation approaches:
- Cross-validation on held-out synthetic data
- Sensitivity analysis across broader parameter ranges
- Comparison with other approximate inference methods

### Task Design
The 5-level conflict paradigm is reasonable but limited:
- How do these λ values map to real-world moral conflicts?
- Would the model generalize to other types of normative tasks?
- Consider multiple task domains in future work

---

## Recommendations for Revision

### Essential (for publication consideration):
1. **Add empirical validation**: Include analysis of at least one real dataset
2. **Strengthen literature review**: Better position NES relative to existing models
3. **Clarify theoretical distinctions**: More precisely define what makes norms computationally distinct
4. **Complete incomplete analyses**: Finish jitter analysis, provide missing technical details

### Strongly Recommended:
1. **Simplify presentation**: Make the paper more accessible to cognitive scientists unfamiliar with SBC
2. **Expand behavioral predictions**: What specific phenomena should NES explain better than alternatives?
3. **Address underdispersion**: Investigate and resolve posterior calibration issues
4. **Improve reproducibility**: Provide complete computational details and code

### Nice to Have:
1. **Multiple task domains**: Validate across different types of normative decisions
2. **Individual differences**: Explore how w_n relates to personality or clinical measures
3. **Neural predictions**: What neural signatures should NES predict?

---

## Minor Editorial Issues

- Page 4: "formalization allows NES to capture hesitation before norm violation" - needs empirical support
- Page 16: "first attempt to estimate w_n directly from human behavior" - this claim needs verification
- Several figures have small fonts that are hard to read
- Some mathematical notation could be clearer (e.g., subscripts and superscripts)
- References formatting needs standardization

---

## Overall Recommendation

This manuscript presents an interesting and potentially important theoretical contribution to computational cognitive science. The technical execution is impressive, particularly for an independent researcher working in this area for the first time. However, the paper currently reads more like a methods/validation paper than a substantive contribution to understanding normative decision-making.

**For publication in a top-tier journal**: Major revisions needed, particularly empirical validation and stronger theoretical grounding.

**For a methods-focused venue**: Minor to moderate revisions needed, focusing on technical completeness and clarity.

**For continued development**: This represents solid foundational work that could develop into a significant contribution with additional empirical validation and theoretical development.

---

## Encouragement and Context

Given your background as a non-academic working independently, this is genuinely impressive work. The technical sophistication, methodological rigor, and novel theoretical insights are commendable. The use of modern techniques like SBC and NPE shows excellent awareness of current best practices in computational modeling.

The main limitations (lack of empirical data, incomplete literature review) are understandable given your constraints and timeline. With continued development, this could become a significant contribution to the field.

Keep up the excellent work, and consider reaching out to academic collaborators who might help with empirical validation and theoretical development.