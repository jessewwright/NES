# Normative Executive System (NES)

This repository contains all code, data, and documentation for the manuscript:

**"Normative Executive System (NES): A Proof-of-Concept Computational Testbed for Identifiable Normative Influence"**  
Author: Jesse Wright  
Date: June 3, 2025

## 📄 Overview

The NES model proposes that normative influence in decision-making is a computationally primitive, architecturally distinct process—separable from utility maximization, salience, or inhibitory control. Using simulation-based inference and parameter recovery techniques, we demonstrate that a dedicated norm weight (`w_n`) is:

- Statistically identifiable via ABC-SMC and Neural Posterior Estimation (NPE)
- Irreducible to traditional drift-diffusion modeling (HDDM) approaches
- Behaviorally distinct in its response to norm–salience conflict

## 📁 Project Structure

```bash
NES_Paper/
├── draft.md              # Main manuscript (Pandoc-compatible Markdown)
├── references.bib        # Bibliography
├── preamble.tex          # Custom LaTeX styling
├── compile.sh            # Compile script to generate PDF
├── paper.pdf             # Final output (optional)
├── src/                  # Model + inference code
├── figures/              # All generated figures
├── data/                 # (Optional) Small anonymized datasets
├── environment.yml       # Conda environment
└── README.md             # You're here
```
