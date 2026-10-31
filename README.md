
# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Deskripsi Proyek

Program ini merupakan aplikasi berbasis terminal menggunakan bahasa Python yang bertujuan membantu guru matematika dalam mengelola dan menganalisis nilai siswa secara otomatis.

Program dikembangkan sebagai proyek akhir mata kuliah Algoritma dan Pemrograman Pertemuan 15.

## 2. Tujuan

- Mempermudah guru dalam merekap nilai siswa.
- Menghitung statistik nilai kelas.
- Menentukan status ketuntasan siswa berdasarkan KKM.
- Menghasilkan laporan hasil analisis nilai.

## 3. Fitur Utama

- Membaca data nilai siswa dari file teks.
- Memvalidasi nilai siswa dalam rentang 0–100.
- Memvalidasi input nilai KKM.
- Menghitung rata-rata nilai.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menampilkan hasil analisis melalui terminal.
- Menyimpan hasil analisis ke file laporan.
- Menangani file tidak ditemukan dan data tidak valid.

## 4. Teknologi

- Bahasa pemrograman: Python 3
- Editor: Visual Studio Code
- Version control: Git dan GitHub

## 5. Struktur Proyek

```text
proyek-akhir-analisis-nilai/
│
├── README.md
├── .gitignore
├── proposal.md
│
├── data/
│   └── nilai_contoh.txt
│
├── output/
│   └── laporan_nilai.txt
│
├── src/
│   ├── analisis.py
│   ├── data_io.py
│   ├── main.py
│   └── utilitas.py
│
└── tests/
    ├── test_analisis.py
    ├── test_data_io.py
    └── test_case.md
```

## 6. Persyaratan

- Python versi 3.x
- Visual Studio Code (disarankan)
- Terminal atau PowerShell

## 7. Cara Menjalankan Program

1. Buka folder proyek menggunakan Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah:

```bash
python -m src.main
```

4. Masukkan nilai KKM ketika diminta.
5. Program akan menampilkan hasil analisis.
6. Laporan akan tersimpan pada folder `output/`.

## 8. Format Data

Data mahasiswa disimpan dalam file:

`data/nilai_contoh.txt`

Format setiap baris:

```text
nama,nilai
```

Contoh:

```text
Ayu,85
Budi,70
Citra,90
Dina,65
```

Nilai harus berada dalam rentang 0 sampai 100.

## 9. Hasil Pengujian

Pengujian dilakukan menggunakan:

- `tests/test_analisis.py`
- `tests/test_data_io.py`

Hasil pengujian terakhir:

| Jenis Pengujian | Jumlah | Hasil |
|---|---:|---|
| Pengujian analisis | 7 | LULUS |
| Pengujian File I/O | 5 | LULUS |
| Total | 12 | LULUS |

Program utama juga berhasil dijalankan menggunakan 8 data mahasiswa.

Contoh hasil analisis dengan KKM 75:

| Keterangan | Hasil |
|---|---:|
| Jumlah mahasiswa | 8 |
| Rata-rata | 77.50 |
| Nilai minimum | 60 |
| Nilai maksimum | 95 |
| Tuntas | 5 |
| Belum tuntas | 3 |

## 10. Known Issues

- Program menggunakan format data teks dengan pemisah koma.
- Data dengan format tidak sesuai akan dilewati dan diberikan pesan kesalahan.
- Program belum menggunakan database.

## 11. Anggota dan Kontribusi

Tuliskan nama anggota kelompok dan pembagian tugas masing-masing sesuai kondisi sebenarnya.

## 12. Referensi/Bantuan

- Materi perkuliahan Algoritma dan Pemrograman Pertemuan 15.
- Dokumentasi Python: https://docs.python.org/3/
- Dokumentasi Git: https://git-scm.com/doc

## 13. Status Proyek

Implementasi fitur inti, integrasi, dan pengujian telah dilakukan.

Dokumentasi dan pemeriksaan akhir repositori dilakukan sebagai tahap penyelesaian proyek.
