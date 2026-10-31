
# TEST CASE
## Program Rekap dan Analisis Nilai Matematika Kelas

### Tujuan Pengujian
Memastikan program dapat membaca data, memvalidasi nilai,
menghitung statistik, menentukan ketuntasan, dan menyimpan laporan.

### Daftar Test Case

| ID | Kategori | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Nilai 80, 70, 90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak |
| TC05 | Invalid | File tidak ditemukan | Data kosong dan pesan kesalahan |
| TC06 | Normal | Nilai 80, 70, 90 dengan KKM 75 | 2 tuntas dan 1 belum tuntas |
| TC07 | Empty | File kosong | Data kosong tanpa program berhenti mendadak |

### Hasil Pengujian Aktual

| ID | Fitur | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| TC01 | Validasi nilai 80, 70, 90 | Valid | Valid | PASS |
| TC02 | Validasi nilai 0 | Valid | Valid | PASS |
| TC03 | Validasi nilai 100 | Valid | Valid | PASS |
| TC04 | Validasi nilai 105 | Ditolak | Ditolak | PASS |
| TC05 | File tidak ditemukan | Data kosong dan pesan kesalahan | Data kosong dan pesan kesalahan | PASS |
| TC06 | Ketuntasan KKM 75 | 2 tuntas, 1 belum tuntas | 2 tuntas, 1 belum tuntas | PASS |
| TC07 | File kosong | Data kosong | Data kosong | PASS |

### Pengujian Tambahan

| ID | Fitur | Hasil Aktual | Status |
|---|---|---|---|
| TA01 | Statistik data kosong | Mengembalikan None | PASS |
| TA02 | Input teks pada validasi nilai | Ditolak | PASS |
| TA03 | Penyimpanan laporan | File berhasil dibuat dan dibaca | PASS |
| TA04 | Data tidak valid dalam file | Baris tidak valid dilewati | PASS |
| TA05 | Program utama | Berjalan dan menghasilkan laporan | PASS |

### Definition of Done

- [x] Semua fitur inti berjalan.
- [x] Pengujian analisis berhasil.
- [x] Pengujian File I/O berhasil.
- [x] Kesalahan input penting ditangani.
- [x] Output mudah dibaca.
- [ ] README diperiksa dan dilengkapi.
- [ ] Perubahan di-commit dan di-push ke GitHub.

### Catatan Pengujian

Pengujian dilakukan menggunakan data simulasi mahasiswa.

Pengujian analisis dilakukan melalui file test_analisis.py.
Pengujian File I/O dilakukan melalui file test_data_io.py.

Seluruh 12 pengujian pada kedua file tersebut berhasil dijalankan.

Program utama juga berhasil dijalankan dengan 8 data mahasiswa
dan KKM 75.

Hasil analisis:
- Jumlah mahasiswa: 8
- Rata-rata: 77.50
- Nilai minimum: 60
- Nilai maksimum: 95
- Jumlah tuntas: 5
- Jumlah belum tuntas: 3
- Laporan berhasil disimpan ke output/laporan_nilai.txt
