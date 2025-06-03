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
