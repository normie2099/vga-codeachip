# Subthreshold Variable-Gain Amplifier Core for Hearing-Aid-Class Audio Compression

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

Submission to the **IEEE SSCS Open-Source Ecosystem "Code-a-Chip" Travel Grant Awards, ISSCC 2027**.

A reproducible, gm/ID-driven automated design flow for a subthreshold variable-gain amplifier (VGA)
core — the gain element of an ultra-low-power hearing-aid audio compressor — implemented entirely
with open-source tools on the SkyWater SKY130 PDK.

> **Scope.** This delivers the **variable-gain core** only. The envelope detector and closed
> gain-control loop are **not** implemented, so no compression ratio, threshold, or attack/release
> characteristic is claimed. Full detail in `notebook.ipynb`, §10.2. This line does not get softened
> or deleted as the project fills in — see the plan doc.

---

## Team

| Name | Affiliation | Role | IEEE / SSCS Member | Email |
|:--|:--|:--|:--:|:--|
| Ayush \<Surname\> | VIT Vellore, India | Lead / travel-grant recipient | \<Yes/No\> | \<email\> |
| \<Team member 2\> | VIT Vellore, India | Co-designer | \<Yes/No\> | \<email\> |
| \<Faculty advisor\> | VIT Vellore, India | Advisor | \<Yes/No\> | \<email\> |

---

## Repository structure

```
vga-codeachip/
├── LICENSE                  # Apache 2.0
├── README.md                # this file
├── notebook.ipynb           # the submission notebook — run this
├── cache/                   # committed: LUTs, optimiser results, environment capture
│   ├── lut_sky130.parquet
│   ├── pareto_results.json
│   └── environment.json
├── netlists/                # xschem exports + testbench templates
├── scripts/                 # importable Python modules (kept out of notebook cells)
│   ├── char.py              # characterisation sweep + parsing
│   ├── lut.py                # LUT interpolators
│   ├── sizing.py             # inverse sizing
│   ├── optimize.py           # pymoo NSGA-II problem
│   └── measure.py            # FoM extraction from raw SPICE output
├── xschem/                  # .sch / .sym schematic sources
├── layout/                  # .mag, .gds, DRC/LVS reports
└── images/                  # every figure used in the notebook/README, committed
```

`cache/` and `images/` are committed on purpose — they're what let a reviewer reproduce every
result without re-running expensive simulations. Raw ngspice output (`.raw`, `.log`) is never
committed; see `.gitignore`.

---

## Reproducing the results

```bash
git clone <this-repo-url>
cd vga-codeachip
# Tools already on $PATH if using IIC-OSIC-TOOLS; otherwise see notebook §2.2 for micromamba install
jupyter notebook notebook.ipynb
# Run top to bottom with default flags (REBUILD_LUT=False) — reproduces
# every result in Sections 5-9 from the cached artefacts in cache/.
```

Target: a clean-room clone should reproduce all figures/tables in under ten minutes. This is
verified twice before submission (see project plan, Phase 7).

---

## Target specification

*Full target table with rationale/citations lives in `notebook.ipynb` Table 2 — this is the
condensed version for anyone browsing the repo first.*

| Parameter | Target | Unit |
|:--|:--:|:--:|
| Supply voltage ($V_{DD}$) | \<1.8\> | V |
| Total quiescent current | \<x\> | µA |
| Mid-band gain range | \<x\> – \<y\> | dB |
| $-3$ dB bandwidth | ≥ \<10\> | kHz |
| Phase margin | ≥ 60 | ° |
| Integrated input noise | ≤ \<x\> | µV$_{rms}$ |
| THD @ \<x\> mV$_{pp}$ | ≤ 1 | % |
| NEF | ≤ \<x\> | – |

---

## Block diagram

`<Insert images/flow.png — the whole flow: characterisation → inverse sizing → Pareto sweep →
verification → layout → post-layout re-verification.>`

---

## Results summary

*Full tables (spec compliance, LUT-vs-SPICE validation, PVT corners, pre/post-layout deltas,
prior-art comparison) are in `notebook.ipynb` §9. Headline numbers only, below — fill in once
Phase 5/6 complete.*

| Metric | Target | Achieved (post-layout, tt/27°C) | Worst corner |
|:--|:--:|:--:|:--:|
| $A_v$ (dB) | | | |
| $I_{tot}$ (µA) | | | |
| $V_{n,rms}$ (µV) | | | |
| NEF | | | |
| DRC | — | \<clean / N errors\> | |
| LVS | — | \<clean / not converged\> | |

---

## Reuse and attribution

| Reused artefact | Source | How it is used here |
|:--|:--|:--|
| gm/ID (C/ID) LUT-driven sizing flow | A. Adair, *Code-a-Chip* ISSCC'25 | Device characterisation and inverse sizing methodology |
| LUT + `pymoo` optimisation structure | A. M. Elhelly, *Code-a-Chip* ISSCC'26 | Multi-objective optimiser wrapper pattern |

This project is a port of a decades-old, clinically-validated circuit function (subthreshold
log-companding hearing-aid AGC, in the lineage of Sarpeshkar-style analog cochlear/hearing-aid
work) onto a fully open PDK — it is **not** presented as a novel circuit. Prior art is cited
directly in `notebook.ipynb` §12.

---

## Tool versions

Pinned versions are captured automatically into `cache/environment.json` during Phase 0 setup
and reproduced in `notebook.ipynb` Table 1. Do not upgrade any tool mid-project — see the risk
register in the plan doc.

---

## License

Licensed under the Apache License, Version 2.0 — see [`LICENSE`](./LICENSE).
SPDX-License-Identifier: `Apache-2.0`

## Acknowledgements

\<Advisor, lab, any mentor — one or two lines.\>
