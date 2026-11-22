import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create output directory for figures
os.makedirs("figures", exist_ok=True)

# ==========================================
# 1. OFFICIAL BENCHMARK DATA (FIGS. 3 - 7)
# ==========================================
protocols = ["LEACH", "HEED", "PEGASIS", "DEC", "Proposed\n(DEC+ACRP)"]

data_main = {
    "Protocol": ["LEACH", "HEED", "PEGASIS", "DEC", "Proposed (DEC+ACRP)"],
    "Network_Lifetime_Percent": [60.0, 62.0, 65.0, 80.0, 90.0],
    "Energy_Efficiency_Percent": [65.0, 68.0, 70.0, 85.0, 92.0],
    "Latency_Seconds": [0.35, 0.32, 0.30, 0.22, 0.15],
    "Privacy_Leakage": [0.25, 0.22, 0.20, 0.12, 0.06],
    "Throughput_PDR_Percent": [68.0, 70.0, 73.0, 85.0, 94.0],
}
df_main = pd.DataFrame(data_main)
df_main.to_csv("protocol_comparison.csv", index=False)

# ==========================================
# 2. SECURITY ATTACK SUCCESS RATES (TABLE 3)
# ==========================================
attacks_data = {
    "Attack_Type": [
        "Brute-Force", "Eavesdropping", "Sybil",
        "Replay Attack", "Wormhole Attack", "Blackhole Attack", "Traffic Analysis"
    ],
    "Baseline_Percent": [85, 92, 68, 74, 58, 62, 77],
    "DEC_Only_Percent": [35, 42, 28, 25, 31, 36, 48],
    "Proposed_DEC_ACRP_Percent": [5, 8, 7, 4, 9, 6, 12],
}
df_attacks = pd.DataFrame(attacks_data)
df_attacks.to_csv("security_attacks.csv", index=False)

# ==========================================
# 3. STATE-OF-THE-ART COMPARISON (TABLE 4)
# ==========================================
sota_data = {
    "Reference": [
        "Prakash et al. (2024)", "Sharma & Gagan (2024)", "Madkar et al. (2024)",
        "Raman et al. (2024)", "Khoshvaght et al. (2025)", "Kumar et al. (2025)",
        "Proposed Method (DEC + ACRP)"
    ],
    "Latency_ms": [10.9, 11.7, 11.0, 11.5, 12.7, 13.9, 2.60],
    "Energy_Consumption_J": [0.84, 0.79, 0.76, 0.80, 0.88, 0.92, 0.21],
    "Network_Lifetime_Percent": [90.9, 91.5, 92.6, 90.3, 89.4, 88.7, 98.3],
    "Throughput_kbps": [120, 119, 124, 117, 112, 108, 152],
    "Scalability": ["High", "High", "High", "High", "High", "Moderate", "High"],
}
df_sota = pd.DataFrame(sota_data)
df_sota.to_csv("sota_comparison.csv", index=False)

# ==========================================
# 4. GENERATE FIGURES (FIGS. 3 - 7 + TABLE 3)
# ==========================================
bar_colors = ["#7f8c8d", "#95a5a6", "#5d6d7e", "#2e86c1", "#1b4f72"]

def plot_bar(values, ylabel, title, filename, ylim, fmt="{:.0f}"):
    plt.figure(figsize=(8, 5))
    bars = plt.bar(protocols, values, color=bar_colors, edgecolor="black", width=0.55)
    for bar, val in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            val + (ylim[1] * 0.02),
            fmt.format(val),
            ha="center", va="bottom", fontsize=10, fontweight="bold"
        )
    plt.ylabel(ylabel, fontsize=11, fontweight="bold")
    plt.xlabel("Routing Protocols", fontsize=11, fontweight="bold")
    plt.title(title, fontsize=12, fontweight="bold")
    plt.ylim(ylim)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(f"figures/{filename}", dpi=300, bbox_inches="tight")
    plt.close()

plot_bar(df_main["Network_Lifetime_Percent"], "Network Lifetime (%)", "Network Lifetime Comparison", "Fig3_Network_Lifetime.png", (0, 105), "{:.0f}%")
plot_bar(df_main["Energy_Efficiency_Percent"], "Energy Efficiency (%)", "Energy Efficiency Comparison", "Fig4_Energy_Efficiency.png", (0, 105), "{:.0f}%")
plot_bar(df_main["Latency_Seconds"], "End-to-End Latency (s)", "End-to-End Latency Comparison", "Fig5_Latency.png", (0, 0.42), "{:.2f}")
plot_bar(df_main["Privacy_Leakage"], "Privacy Leakage", "Privacy Leakage Comparison", "Fig6_Privacy_Leakage.png", (0, 0.30), "{:.2f}")
plot_bar(df_main["Throughput_PDR_Percent"], "Throughput / PDR (%)", "Packet Delivery Rate Comparison", "Fig7_Throughput_PDR.png", (0, 108), "{:.0f}%")

# Security Attack Success Rates Chart (Table 3)
x = np.arange(len(df_attacks["Attack_Type"]))
width = 0.25

plt.figure(figsize=(10, 5.5))
plt.bar(x - width, df_attacks["Baseline_Percent"], width, label="Baseline", color="#c0392b", edgecolor="black")
plt.bar(x, df_attacks["DEC_Only_Percent"], width, label="DEC-Only", color="#f39c12", edgecolor="black")
plt.bar(x + width, df_attacks["Proposed_DEC_ACRP_Percent"], width, label="Proposed (DEC+ACRP)", color="#1b4f72", edgecolor="black")

plt.ylabel("Attack Success Rate (%)", fontsize=11, fontweight="bold")
plt.title("Security Attack Success Rates Across Protocols (Lower is Better)", fontsize=12, fontweight="bold")
plt.xticks(x, df_attacks["Attack_Type"], rotation=20, ha="right", fontsize=10)
plt.ylim(0, 105)
plt.legend(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/Fig8_Attack_Success_Rates.png", dpi=300, bbox_inches="tight")
plt.close()

print("Done! Generated 3 CSV files and 6 figures in /figures.")