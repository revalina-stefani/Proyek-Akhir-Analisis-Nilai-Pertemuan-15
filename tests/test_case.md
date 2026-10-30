
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
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi |
| TC05 | Invalid | File tidak ditemukan | Pesan kesalahan ditampilkan |
| TC06 | Normal | Semua nilai >= KKM | Semua siswa dinyatakan tuntas |
| TC07 | Invalid | File kosong | Pesan tidak ada data valid |

### Definition of Done

- [ ] Semua fitur wajib berjalan.
- [ ] Semua test case lulus.
- [ ] Kesalahan input dapat ditangani.
- [ ] Output mudah dibaca.
- [ ] README menjelaskan cara menjalankan program.
- [ ] Riwayat commit GitHub menunjukkan perkembangan proyek.

### Catatan Pengujian
Pengujian dilakukan menggunakan data simulasi.
Hasil aktual akan dicatat setelah program selesai diimplementasikan.


## Hasil Pengujian Aktual

| ID | Hasil Pengujian | Status |
|---|---|---|
| TC01 | Membaca dan menghitung data normal | Menunggu pengujian |
| TC02 | Nilai 0 diterima | Menunggu pengujian |
| TC03 | Nilai 100 diterima | Menunggu pengujian |
| TC04 | Nilai 105 ditolak | Menunggu pengujian |
| TC05 | File tidak ditemukan ditangani | Menunggu pengujian |
| TC06 | Ketuntasan dihitung dengan benar | Menunggu pengujian |
| TC07 | File kosong ditangani | Menunggu pengujian |
