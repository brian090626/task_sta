#visualization 

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.signal import spectrogram
import numpy as np

# Load dataset
file_path = "datasta.csv"  # Replace with your actual file path
data = pd.read_csv(file_path)

# Ensure proper formatting of column names if needed
if data.columns[0].startswith("Unnamed"):
    data.columns = [f"Feature_{i}" for i in range(data.shape[1])]

# 1. Time Series Line Plot
plt.figure(figsize=(12, 6))
for i in range(3):
    plt.plot(range(100), data.iloc[i, :100], label=f"Signal {i+1}", linewidth=2)
plt.title("Time Series Line Plot", fontsize=18, fontweight='bold')
plt.xlabel("Time (Feature Index)", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.legend(fontsize=12)
plt.grid(linestyle='--', alpha=0.6)
plt.savefig("time_series_line_plot.png")
plt.close()

# 2. Histogram of Amplitude Distribution
plt.figure(figsize=(12, 6))
amplitudes = data.values.flatten()
sns.histplot(amplitudes, bins=50, kde=True, color="blue", alpha=0.7)
plt.title("Amplitude Distribution", fontsize=18, fontweight='bold')
plt.xlabel("Amplitude", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(linestyle='--', alpha=0.6)
plt.savefig("amplitude_histogram.png")
plt.close()

# 3. Box Plot of Feature Distribution
plt.figure(figsize=(12, 6))
data.iloc[:, :50].boxplot()
plt.title("Box Plot of First 50 Features", fontsize=18, fontweight='bold')
plt.xlabel("Feature Index", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.grid(linestyle='--', alpha=0.6)
plt.savefig("box_plot.png")
plt.close()

# 4. Spectrogram for Signal Analysis
plt.figure(figsize=(12, 6))
f, t, Sxx = spectrogram(data.iloc[0].values, fs=1.0)
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
plt.colorbar(label='Power (dB)')
plt.title("Spectrogram", fontsize=18, fontweight='bold')
plt.xlabel("Time", fontsize=14)
plt.ylabel("Frequency (Hz)", fontsize=14)
plt.savefig("spectrogram.png")
plt.close()

# 5. Scatter Plot for Feature Correlation
plt.figure(figsize=(12, 6))
plt.scatter(data.iloc[:, 0], data.iloc[:, 1], alpha=0.7, color='red', edgecolor='black')
plt.title("Scatter Plot of Feature 1 vs Feature 2", fontsize=18, fontweight='bold')
plt.xlabel("Feature 1", fontsize=14)
plt.ylabel("Feature 2", fontsize=14)
plt.grid(linestyle='--', alpha=0.6)
plt.savefig("scatter_plot.png")
plt.close()

# Output paths
print("Generated files:")
print("1. time_series_line_plot.png")
print("2. amplitude_histogram.png")
print("3. box_plot.png")
print("4. spectrogram.png")
print("5. scatter_plot.png")