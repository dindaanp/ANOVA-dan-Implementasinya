# Studi Kasus 2: Efektivitas Obat terhadap Penurunan Tekanan Darah

import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/data_obat.csv")

# Visualisasi
sns.boxplot(x="Obat", y="Penurunan", data=df)
plt.title("Penurunan Tekanan Darah oleh Masing-masing Obat")
plt.show()

# ANOVA
a = df[df["Obat"]=="A"]["Penurunan"]
b = df[df["Obat"]=="B"]["Penurunan"]
c = df[df["Obat"]=="C"]["Penurunan"]

f_stat, p_val = stats.f_oneway(a, b, c)

print(f"F-statistik: {f_stat:.3f}")
print(f"P-value: {p_val:.3f}")

if p_val < 0.05:
    print("Terdapat perbedaan signifikan efektivitas antar obat.")
else:
    print("Tidak terdapat perbedaan signifikan efektivitas antar obat.")
