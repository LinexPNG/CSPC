import pandas as pd
import numpy as np
from scipy import stats

df_chem = pd.read_csv("chemicals_cancer.csv")
print("Chemicals Data shape:", df_chem.shape)

r_benz_naive, _ = stats.pearsonr(df_chem["benzene"], df_chem["malignancy"])
r_cadm_naive, _ = stats.pearsonr(df_chem["cadmium"], df_chem["malignancy"])

print("\n--- Naive Analysis ---")
print(f"Benzene vs Malignancy r: {r_benz_naive:.4f}")
print(f"Cadmium vs Malignancy r: {r_cadm_naive:.4f}")

p_low = df_chem["pollution_index"].quantile(0.4)
p_high = df_chem["pollution_index"].quantile(0.6)

df_restricted = df_chem[(df_chem["pollution_index"] >= p_low) & (df_chem["pollution_index"] <= p_high)]

r_benz_adj, _ = stats.pearsonr(df_restricted["benzene"], df_restricted["malignancy"])
r_cadm_adj, _ = stats.pearsonr(df_restricted["cadmium"], df_restricted["malignancy"])

print("\n--- Adjusted Analysis (Restricted Pollution Index Range) ---")
print(f"Benzene vs Malignancy r (controlled): {r_benz_adj:.4f}")
print(f"Cadmium vs Malignancy r (controlled): {r_cadm_adj:.4f}")

df_heart = pd.read_csv("heart.csv")
probs = df_heart["target"].value_counts(normalize=True)
entropy = -np.sum(probs * np.log2(probs))
print(f"\n--- Bonus Task ---")
print(f"Target Distribution:\n{probs}")
print(f"Binary Entropy of Target: {entropy:.4f} bits")