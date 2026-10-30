PROPOSAL PROYEK AKHIR
Program Rekap dan Analisis Nilai Matematika Kelas
1. Judul Proyek

Program Rekap dan Analisis Nilai Matematika Kelas.

2. Latar Belakang Masalah

Dalam kegiatan pembelajaran matematika, guru perlu mengelola dan merekap nilai siswa untuk mengetahui hasil belajar dan tingkat ketuntasan siswa. Proses penghitungan nilai secara manual membutuhkan waktu dan berisiko menimbulkan kesalahan perhitungan.

Oleh karena itu, diperlukan program sederhana berbasis Python yang dapat membantu guru membaca data nilai, menghitung statistik, menentukan status ketuntasan, dan menyimpan laporan secara otomatis.

3. Pengguna dan Tujuan

Pengguna utama: Guru matematika.

Tujuan proyek:

Mempermudah proses rekapitulasi nilai siswa.
Menghitung statistik nilai secara otomatis.
Menentukan status ketuntasan berdasarkan KKM.
Menghasilkan laporan nilai yang mudah dibaca.
4. Ruang Lingkup Proyek

Fitur wajib:

Membaca data nilai siswa dari file.
Memvalidasi nilai dalam rentang 0–100.
Menghitung rata-rata, nilai minimum, dan maksimum.
Menentukan status tuntas dan belum tuntas berdasarkan KKM.
Menyimpan laporan hasil analisis ke file teks.

Batasan proyek:

Program dijalankan melalui terminal atau console.
Menggunakan bahasa pemrograman Python.
Tidak menggunakan database.
Tidak menggunakan antarmuka web atau grafis.
Data pengujian menggunakan data siswa simulasi.
5. Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional:

F01: Program dapat membaca data nilai dari file.
F02: Program dapat memvalidasi nilai 0–100.
F03: Program dapat menghitung rata-rata, minimum, dan maksimum.
F04: Program dapat menentukan status ketuntasan siswa berdasarkan KKM.
F05: Program dapat menyimpan laporan hasil analisis.

Kebutuhan nonfungsional:

Program mudah dijalankan melalui terminal VS Code.
Pesan kesalahan mudah dipahami.
Nama fungsi dan variabel mudah dimengerti.
Data contoh tidak menggunakan informasi pribadi nyata.
Program dapat diuji ulang menggunakan test case yang sama.

6. Spesifikasi Input, Proses, dan Output (IPO)

A. Input

Input yang digunakan dalam program adalah:

File nilai_contoh.txt yang berisi data nama dan nilai siswa.
Nilai KKM sebagai batas ketuntasan belajar.

B. Proses

Program akan melakukan proses berikut:

Membaca data nilai siswa dari file.
Memeriksa format data dan validitas nilai.
Menyimpan data yang valid ke dalam struktur list atau dictionary.
Menghitung rata-rata, nilai minimum, dan maksimum.
Menentukan status tuntas atau belum tuntas berdasarkan KKM.
Menyiapkan laporan hasil analisis.

C. Output

Output yang dihasilkan program adalah:

- Daftar data siswa yang valid.
- Rata-rata nilai kelas.
- Nilai minimum dan maksimum.
- Jumlah siswa tuntas dan belum tuntas.
- Status ketuntasan setiap siswa.
- File laporan hasil analisis pada `output/laporan_nilai.txt`.


7. Algoritma dan Pseudocode

Pseudocode Program Rekap dan Analisis Nilai Matematika Kelas

text
MULAI

Tentukan lokasi file nilai
Tentukan nilai KKM

Baca data dari file

JIKA file tidak ditemukan:
    Tampilkan pesan "File tidak ditemukan"
    SELESAI

Buat daftar data valid
Buat daftar data tidak valid

UNTUK setiap baris data:
    Periksa format data

    JIKA format data benar:
        Ambil nama dan nilai

        JIKA nilai berada pada rentang 0 sampai 100:
            Simpan data ke daftar data valid
        JIKA TIDAK:
            Catat data sebagai tidak valid
    JIKA TIDAK:
        Catat data sebagai tidak valid

JIKA daftar data valid kosong:
    Tampilkan pesan "Tidak ada data valid"
    SELESAI

Hitung rata-rata nilai
Cari nilai minimum
Cari nilai maksimum

Hitung jumlah siswa tuntas
Hitung jumlah siswa belum tuntas

Tampilkan hasil analisis
Tampilkan data tidak valid jika ada

Simpan hasil analisis ke file laporan.txt

SELESAI

8. Struktur Program dan Modularisasi

Program dibagi menjadi beberapa fungsi agar setiap bagian memiliki tanggung jawab yang jelas.


Program dibagi menjadi beberapa fungsi agar setiap bagian memiliki tanggung jawab yang jelas.

| Fungsi | Tanggung Jawab | Input | Output |
|---|---|---|---|
| baca_data() | Membaca dan memvalidasi data siswa dari file | Path file | List data siswa valid |
| validasi_nilai() | Memeriksa rentang nilai 0–100 | Nilai | True/False |
| hitung_statistik() | Menghitung rata-rata, minimum, dan maksimum | Data nilai | Dictionary statistik |
| tentukan_status() | Menentukan status ketuntasan siswa | Nilai dan KKM | Status siswa |
| simpan_laporan() | Menyimpan hasil analisis ke file | Isi laporan dan path | File laporan |
| main() | Mengatur seluruh alur program | - | Hasil program |



proyek-akhir-analisis-nilai/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_contoh.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   ├── test_case.md
│   ├── test_analisis.py
│   └── test_data_io.py
│
└── output/
    └── laporan_nilai.txt




Prinsip modularisasi digunakan untuk memisahkan proses pembacaan data, pengolahan nilai, dan pengelolaan hasil laporan agar program lebih mudah diuji dan diperbaiki.


9. Pemilihan Struktur Data

Struktur data yang digunakan dalam program ini adalah:

| Struktur Data | Penggunaan | Alasan |
|---|---|---|
| List | Menyimpan kumpulan data siswa dan nilai | Memudahkan iterasi dan perhitungan statistik |
| Dictionary | Menyimpan atribut siswa seperti nama dan nilai | Memudahkan akses data berdasarkan key |
| String | Menyimpan nama, pesan, dan teks laporan | Memudahkan pengolahan teks |
| File | Membaca data nilai dan menyimpan laporan | Memungkinkan data disimpan secara permanen |

Contoh model data:

```python
data_mahasiswa = [
    {"nama": "Ayu", "nilai": 85},
    {"nama": "Budi", "nilai": 78}
]
```

Struktur data tersebut dipilih karena sederhana, sesuai dengan materi Python yang dipelajari, dan dapat mendukung seluruh fitur wajib proyek.

10. Perancangan Test Case

Pengujian dilakukan untuk memastikan seluruh fitur program berjalan sesuai kebutuhan. Test case mencakup kondisi normal, batas, dan invalid.

ID	Kategori	Input/Kondisi	Hasil yang Diharapkan
TC01	Normal	Nilai 80, 70, 90	Rata-rata 80
TC02	Batas	Nilai 0	Diterima sebagai nilai valid
TC03	Batas	Nilai 100	Diterima sebagai nilai valid
TC04	Invalid	Nilai 105	Ditolak dengan pesan validasi
TC05	Invalid	File tidak ditemukan	Program menampilkan pesan kesalahan
TC06	Normal	Semua nilai lebih besar atau sama dengan KKM	Jumlah siswa tuntas sama dengan jumlah data valid
TC07	Invalid	File kosong atau tidak memiliki data valid	Program menampilkan pesan bahwa tidak ada data valid

Pengujian akan dilakukan menggunakan data simulasi agar hasilnya dapat diperiksa dan diulang.

Definition of Done:

Semua fitur wajib berjalan.
Semua test case wajib lulus.
Program dapat menangani kesalahan input yang telah diperkirakan.
Output mudah dibaca.
README menjelaskan cara menjalankan program.
Riwayat commit GitHub menunjukkan perkembangan proyek.

11. Pembagian Tugas dan Tanggung Jawab

Proyek ini dikerjakan secara individu. Seluruh proses perancangan, implementasi, pengujian, dan dokumentasi dilakukan oleh satu orang.

Peran	Tanggung Jawab
Perancang Proyek	Menentukan masalah, tujuan, dan ruang lingkup proyek
Programmer	Membuat program Python dan mengembangkan seluruh fitur
Pengelola Data	Membuat dan mengelola file data nilai siswa
Tester/QA	Menyusun dan menjalankan test case serta memperbaiki kesalahan program
Dokumentasi	Menyusun proposal, README, dan dokumentasi GitHub

Penanggung Jawab: Revalina Stefani

12. Jadwal Pengerjaan (Milestone)
Waktu	Target Pengerjaan
Pertemuan 14	Menyelesaikan proposal, pseudocode, struktur program, dan test case
Antara P14–P15	Membuat implementasi awal fitur wajib
Pertemuan 15	Integrasi program, pengujian, debugging, dan dokumentasi
Pertemuan 16	Presentasi, demonstrasi program, dan evaluasi proyek


## 13. Repository GitHub

Repository proyek digunakan sebagai tempat penyimpanan kode program, data contoh, dokumentasi, dan test case.

- Platform: GitHub
- Nama repository: proyek-akhir-analisis-nilai
- URL repository: https://github.com/revalina-stefani/proyek-akhir-analisis-nilai
- Branch utama: main

Repository digunakan untuk mencatat perkembangan proyek melalui commit sehingga setiap perubahan dapat ditelusuri.

