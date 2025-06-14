# Analisis ANOVA dan Penerapannya dalam Python

Repositori ini membahas tentang **Analisis Varian (ANOVA)**, sebuah metode statistik yang digunakan untuk membandingkan rata-rata dari tiga atau lebih kelompok. Materi ini disusun dalam Bahasa Indonesia, dilengkapi dengan **dua studi kasus orisinal** dan penerapannya dalam Python.

## Apa itu ANOVA?

ANOVA (Analysis of Variance) adalah metode statistik yang digunakan untuk menguji apakah terdapat perbedaan yang signifikan antara rata-rata dari tiga kelompok atau lebih. Jika kita hanya memiliki dua kelompok, kita bisa menggunakan uji t, namun jika ada tiga atau lebih, ANOVA adalah metode yang tepat.

## Tujuan Utama ANOVA
Tujuan utama ANOVA adalah untuk menguji apakah perbedaan rata-rata antar kelompok adalah signifikan secara statistik. ANOVA bekerja dengan membandingkan variasi antar kelompok (antara mean kelompok) dengan variasi di dalam kelompok (antar individu dalam satu kelompok).

## Jenis-jenis ANOVA
1. **One-way ANOVA**: Satu variabel independen (faktor).
2. **Two-way ANOVA**: Dua faktor dan dapat memperhitungkan interaksi antar faktor.

## Konsep Dasar ANOVA
Dalam ANOVA, total variasi dalam data dibagi menjadi dua bagian:
1. **Variasi antar kelompok (Between-group variability)**  
Variasi ini menunjukkan seberapa besar perbedaan rata-rata antar kelompok.
2. **Variasi dalam kelompok (Within-group variability)**  
Variasi ini menggambarkan seberapa besar variasi data individu dalam satu kelompok yang sama.

Semakin besar variasi antar kelompok dibandingkan variasi dalam kelompok, semakin mungkin bahwa rata-rata kelompok memang berbeda secara signifikan.

## Kontribusi Analisis Nova
Mengapa Variasi Antar dan Dalam Kelompok Penting?
Membandingkan variasi antar kelompok dengan dalam kelompok penting untuk memastikan perbedaan antar kelompok lebih signifikan daripada fluktuasi acak dalam kelompok.

Penerapan ANOVA di Berbagai Bidang
Pemasaran: Menguji dampak kampanye terhadap penjualan.
Medis: Menilai efektivitas pengobatan.
Industri: Memeriksa kualitas produk dari berbagai pabrik.

Kekuatan dan Kelemahan ANOVA
Kekuatan: Menguji perbedaan antar banyak kelompok.
Kelemahan: Memerlukan asumsi normalitas dan kesamaan variansi. Jika dilanggar, uji non-parametrik bisa dipilih.

## Rumus Dasar

Nilai statistik ANOVA (F) dihitung sebagai:

**F = Variansi antar kelompok / Variansi dalam kelompok**

Jika nilai p-value dari F lebih kecil dari 0.05 (tingkat signifikansi), maka dapat disimpulkan bahwa terdapat perbedaan yang signifikan antara kelompok.

## Asumsi ANOVA
Agar hasil ANOVA valid, terdapat beberapa asumsi dasar yang harus dipenuhi:

1. **Independensi**: Data antar pengamatan harus bebas satu sama lain.
2. **Normalitas**: Distribusi data dalam tiap kelompok harus mendekati distribusi normal.
3. **Homoskedastisitas (Homogeneity of Variance)**: Variansi antar kelompok harus seragam.  

Jika asumsi ini dilanggar, maka hasil uji ANOVA bisa tidak valid dan uji non-parametrik seperti Kruskal-Wallis bisa dipertimbangkan sebagai alternatif.
