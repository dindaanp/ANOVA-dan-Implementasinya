# Studi Kasus 1: Pengaruh Departemen terhadap Kepuasan Kerja

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/data_karyawan.csv")

# Visualisasi
sns.boxplot(x="Departemen", y="Kepuasan", data=df)
plt.title("Boxplot Kepuasan Kerja per Departemen")
plt.show()

# ANOVA
hr = df[df["Departemen"]=="HR"]["Kepuasan"]
it = df[df["Departemen"]=="IT"]["Kepuasan"]
mkt = df[df["Departemen"]=="Marketing"]["Kepuasan"]

f_stat, p_val = stats.f_oneway(hr, it, mkt)

print(f"F-statistik: {f_stat:.3f}")
print(f"P-value: {p_val:.3f}")

if p_val < 0.05:
    print("Terdapat perbedaan signifikan antar departemen.")
else:
    print("Tidak terdapat perbedaan signifikan antar departemen.")
