import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df_heart = pd.read_csv("heart.csv")
print("Data shape:", df_heart.shape)
print("First 5 rows:\n", df_heart.head())

cont_cols = ["age", "chol", "trestbps", "thalach"]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

for i, col in enumerate(cont_cols):
    axes[i].hist(df_heart[col], bins=20, color='skyblue', edgecolor='black', density=True)
    
    mu, std = stats.norm.fit(df_heart[col])
    xmin, xmax = axes[i].get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    axes[i].plot(x, p, 'r-', linewidth=2)
    
    axes[i].set_title(f"Distribution of {col}")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Density")

plt.tight_layout()
plt.savefig("heart_distributions.png")
plt.close()

print("\n--- Normality Tests (Shapiro-Wilk) ---")
for col in cont_cols:
    stat, p_val = stats.shapiro(df_heart[col])
    verdict = "Normal" if p_val > 0.05 else "Non-Normal"
    print(f"{col}: W={stat:.4f}, p={p_val:.4e} -> {verdict}")

healthy_thalach = df_heart[df_heart["target"] == 0]["thalach"]
disease_thalach = df_heart[df_heart["target"] == 1]["thalach"]

stat_tw, p_val_tw = stats.ttest_ind(healthy_thalach, disease_thalach)
print(f"\nTwo-sample t-test (thalach): t={stat_tw:.4f}, p={p_val_tw:.4e}")

mean_h, sem_h = healthy_thalach.mean(), healthy_thalach.sem()
mean_d, sem_d = disease_thalach.mean(), disease_thalach.sem()

print(f"Healthy thalach: {mean_h:.2f} +/- {sem_h:.2f} (SEM)")
print(f"Disease thalach: {mean_d:.2f} +/- {sem_d:.2f} (SEM)")

plt.figure(figsize=(6, 5))
plt.bar(["Healthy (0)", "Disease (1)"], [mean_h, mean_d], yerr=[1.96*sem_h, 1.96*sem_d], capsize=5, color=['green', 'darkred'])
plt.ylabel("Mean Max Heart Rate (thalach)")
plt.title("Thalach by Heart Disease Status (95% CI)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("thalach_comparison.png")
plt.close()

corr_pearson, p_p = stats.pearsonr(df_heart["age"], df_heart["thalach"])
corr_spearman, p_s = stats.spearmanr(df_heart["age"], df_heart["thalach"])
print(f"\nAge vs Thalach Correlation:")
print(f"Pearson: r={corr_pearson:.4f}, p={p_p:.4e}")
print(f"Spearman: rho={corr_spearman:.4f}, p={p_s:.4e}")

plt.figure(figsize=(7, 5))
plt.scatter(df_heart["age"], df_heart["thalach"], alpha=0.6, color='purple')
m, b = np.polyfit(df_heart["age"], df_heart["thalach"], 1)
plt.plot(df_heart["age"], m*df_heart["age"] + b, color='red', linewidth=2)
plt.xlabel("Age")
plt.ylabel("Max Heart Rate (thalach)")
plt.title("Age vs Max Heart Rate")
plt.grid(True)
plt.savefig("age_vs_thalach.png")
plt.close()