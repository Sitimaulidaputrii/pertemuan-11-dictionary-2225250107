# Pertemuan 11 - Dictionary/Map

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Memodelkan data mahasiswa menggunakan dictionary serta mengolah data berdasarkan pasangan key dan value.

## Struktur Data

Dictionary data_mahasiswa menggunakan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa. Struktur ini memudahkan pencarian, penambahan, pembaruan, dan penampilan data mahasiswa.

## Cara Menjalankan

Program praktik dapat dijalankan melalui Terminal VS Code dengan perintah:
```bash
python praktik/data_mahasiswa.py
```

untuk menjalankan program latihan:
```bash
python latihan/01_dasar_dictionary.py
```

untuk menjalankan yang lainnya, gunakan perintah sesuai dengan nama berkasnya.

## Test Case

| Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| --- | --- | --- | --- |
| Pencarian NIM A003 | Data Citra ditampilkan | Data Citra berhasil ditampilkan | Berhasil |
| Pencarian NIM A999 | Pesan data tidak ditemukan | Data tidak ditemukan | Berhasil |
| Mengubah nilai A002 menjadi 82 | Nilai A002 berubah menjadi 82 | Nilai A002 berubah menjadi 82 | Berhasil |
| Menambahkan mahasiswa A006 | Data mahasiswa A006 tersimpan | Data A006 berhasil ditambahkan | Berhasil |
| Menampilkan seluruh data dengan items() | Semua data mahasiswa ditampilkan | Berhasil |
| Menghitung rata-rata nilai | Rata-rata sebesar 83.50 | Rata-rata = 83.50 | Berhasil |

## Refleksi

Kesalahan yang ditemukan adalah penempatan return di dalam perulangan pada fungsi rata_rata_nilai(). Akibatnya, perhitungan berhenti setelah membaca nilai mahasiswa pertama. Kesalahan tersebut diperbaiki dengan memindahkan return ke luar perulangan agar seluruh nilai dijumlahkan sebelum menghitung rata-rata.