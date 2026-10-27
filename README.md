# Pertemuan 11 - Dictionary/Map

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Memodelkan data mahasiswa menggunakan dictionary serta mengolah data berdasarkan pasangan key dan value.

## Struktur Data

Dictionary data_mahasiswa menggunakan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa. Struktur ini memudahkan pencarian, penambahan, pembaruan, dan penampilan data mahasiswa.

## Cara Menjalankan



## Test Case



## Refleksi

Kesalahan yang ditemukan adalah penempatan return di dalam perulangan pada fungsi rata_rata_nilai(). Akibatnya, perhitungan berhenti setelah membaca nilai mahasiswa pertama. Kesalahan tersebut diperbaiki dengan memindahkan return ke luar perulangan agar seluruh nilai dijumlahkan sebelum menghitung rata-rata.