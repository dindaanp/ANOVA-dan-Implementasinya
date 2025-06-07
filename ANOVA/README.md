# Analisis ANOVA dan Penerapannya dalam Python

Repositori ini membahas tentang **Analisis Varian (ANOVA)**, sebuah metode statistik yang digunakan untuk membandingkan rata-rata dari tiga atau lebih kelompok. Materi ini disusun dalam Bahasa Indonesia, dilengkapi dengan **dua studi kasus orisinal** dan penerapannya dalam Python.

## Apa itu ANOVA?

ANOVA (Analysis of Variance) adalah metode statistik yang digunakan untuk menguji apakah terdapat perbedaan yang signifikan antara rata-rata dari tiga kelompok atau lebih. Jika kita hanya memiliki dua kelompok, kita bisa menggunakan uji t, namun jika ada tiga atau lebih, ANOVA adalah metode yang tepat.

### Rumus Dasar

Nilai statistik ANOVA (F) dihitung sebagai:

**F = Variansi antar kelompok / Variansi dalam kelompok**

Jika nilai p-value dari F lebih kecil dari 0.05 (tingkat signifikansi), maka dapat disimpulkan bahwa terdapat perbedaan yang signifikan antara kelompok.

## Instalasi Library

Pastikan Anda telah menginstal library berikut:

```bash
pip install pandas numpy scipy statsmodels matplotlib seaborn
```

## Studi Kasus

Repositori ini mencakup dua studi kasus:

1. **Pengaruh Departemen terhadap Kepuasan Kerja Karyawan** (`studi_kasus_1.ipynb`)
2. **Efektivitas Tiga Jenis Obat terhadap Penurunan Tekanan Darah** (`studi_kasus_2.ipynb`)

## Lisensi

Materi ini dirilis dengan lisensi MIT.
