#Buat gambar population_vs_sample_kde_plot

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data for population and sample
np.random.seed(42)  # For reproducibility
population = np.random.normal(loc=0, scale=0.1, size=1000)  # Population data
sample = np.random.choice(population, size=200, replace=False)  # Sample data

# Enhanced Population vs Sample Distribution with KDE overlay
plt.figure(figsize=(12, 8))

# Histogram and KDE for Population
sns.histplot(population, bins=50, kde=True, color='yellow', label='Population', stat="frequency", alpha=0.6, edgecolor="black")

# Histogram and KDE for Sample
sns.histplot(sample, bins=50, kde=True, color='grey', label='Sample (20%)', stat="frequency", alpha=0.6, edgecolor="black")

# Add titles and labels
plt.title("Population vs Sample Distribution with KDE", fontsize=18, fontweight='bold')
plt.xlabel("Value", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

# Add legend
plt.legend(fontsize=12, loc="upper right")

# Save the enhanced plot
plt.savefig("population_vs_sample_kde_plot.png")
plt.show()
