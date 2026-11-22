# WBSN-DEC-ACRP-Privacy-Benchmark

Official benchmark datasets, security evaluation metrics, and 300-DPI figure reproduction scripts for our **Springer CCIS (2026)** article:

> **Enhanced Energy-Efficient and Privacy-Preserving Routing Framework for Wireless Body Sensor Networks Using Deep Embedded Clustering and Adaptive Context-Aware Protocols**  
> *Tuqa Kareem Jebur, Lourdes Peñalver, Jaime Lloret, and Haider K. Hoomod*  
> In: S. O. Al-Mamory et al. (Eds.), *3INC 2025*, Communications in Computer and Information Science (CCIS), Vol. 2960, pp. 130–149, Springer, 2026.  
> **DOI:** [10.1007/978-3-032-24239-6_9](https://doi.org/10.1007/978-3-032-24239-6_9)

---

## Key Performance Highlights (DEC + ACRP)
Evaluated on real physiological datasets (**PhysioNet** and **MHEALTH**) across 100 sensor nodes over 7,000 simulation rounds:

| Metric | Proposed (DEC + ACRP) | Key Advantage |
| :--- | :---: | :--- |
| **Network Lifetime** | **90%** (98.3% vs. SOTA) | +25–30% increase over traditional protocols |
| **Energy Efficiency** | **92%** | +41.5% relative gain over LEACH (65%) |
| **End-to-End Latency** | **0.15 s** (2.60 ms vs. SOTA) | -57.1% reduction compared to LEACH (0.35 s) |
| **Privacy Leakage** | **0.06** | -76% reduction via $\epsilon$-differential privacy |
| **Packet Delivery Rate (PDR)** | **94%** | Highest reliability across all tested baselines |
| **Security Resistance** | **>93% Brute-Force \| >88% Eavesdropping** | Quantum-inspired randomized routing |

---

## Repository Contents
* `protocol_comparison.csv` — Comparative metrics (Figs. 3–7) against LEACH, HEED, PEGASIS, and DEC.
* `security_attacks.csv` — Attack success rates across 7 threat vectors (Table 3).
* `sota_comparison.csv` — Comparison against 2024–2025 state-of-the-art WBSN routing protocols (Table 4).
* `reproduce_figures.py` — Standalone Python script to regenerate all figures at 300 DPI.
* `figures/` — High-resolution PNG charts of performance and security evaluations.

---

## How to Cite
If you use these benchmark datasets or figures in your research, please cite our work:

```bibtex
@INPROCEEDINGS{Jebur2026DECACRP,
  author={Jebur, Tuqa Kareem and Peñalver, Lourdes and Lloret, Jaime and Hoomod, Haider K.},
  editor={Al-Mamory, Safaa O. and others},
  title={Enhanced Energy-Efficient and Privacy-Preserving Routing Framework for Wireless Body Sensor Networks Using Deep Embedded Clustering and Adaptive Context-Aware Protocols},
  booktitle={3INC 2025, Communications in Computer and Information Science (CCIS)},
  year={2026},
  publisher={Springer Nature Switzerland},
  volume={2960},
  pages={130--149},
  doi={10.1007/978-3-032-24239-6_9}
}
