def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)

data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# Pencarian Mahasiswa
nim = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

nim = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim)

if hasil is not None:
    print(f"{nim}: {hasil}")
else:
    print("Data tidak ditemukan")

# Penambahan mahasiswa baru
data_mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "B",
    "nilai": 80
}
print("Mahasiswa A006 berhasil ditambahkan.")

# Pembaruan nilai mahasiswa
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi berhasil diubah menjadi", data_mahasiswa["A002"]["nilai"])

# Rekap seluruh data mahasiswa
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim}, Nama: {info['nama']}, Kelas: {info['kelas']}, Nilai: {info['nilai']}")

# Perhitungan rata-rata nilai
print(f"Rata-rata = {rata_rata_nilai(data_mahasiswa):.2f}")