---
title: "Normative Executive System (NES): A Proof-of-Concept Computational Testbed for Identifiable Normative Influence"
author: Jesse Wright
date: "May 8, 2025"
bibliography: references.bib
link-citations: true
fontsize: 11pt
geometry: margin=1in
header-includes:
  - \usepackage{graphicx}
  - \graphicspath{{./figures/}}
  - \usepackage{hyperref}
  - \hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue}
  - \usepackage{parskip}
  - \setlength{\parskip}{0.25\baselineskip}
  - \renewcommand{\bfdefault}{b}
  - \renewcommand{\bfseries}{\mdseries\bfseries}
---

# Introduction

We propose that normative influence in human decision-making is computationally primitive—not emergent from utility maximization, emotional response, or social learning—but a fundamental architectural component of moral cognition. To test this theoretical claim, we introduce the Normative Executive System (NES), extending the Drift Diffusion Model with an explicit norm weight parameter ($w_n$) that modulates decision dynamics independently of utility-based signals.

## Background

NES builds on a rich tradition of cognitive modeling, including the conflict monitoring framework [@Botvinick2001ConflictMonitoring], dual-process theories of moral judgment [@Greene2001fMRI], and attribute-wise value integration models [@Hare2009SelfControl]. However, these models either lack explicit norm representations or do not validate the identifiability of such constructs from behavior.

## Methods

Our empirical test employs Simulation-Based Calibration across multiple inference methods (ABC-SMC and Neural Posterior Estimation), revealing the key finding that $w_n$ is statistically identifiable from behavioral data, suggesting normative influence leaves distinct computational signatures unexplained by existing models.

## References
