
from data_io import baca_data, simpan_laporan

from analisis import (
    hitung_statistik,
    hitung_ketuntasan
)

from utilitas import (
    tampilkan_judul,
    tampilkan_data,
    buat_laporan
)


def main():
    tampilkan_judul()

    # Lokasi file data
    path_data = "data/nilai_contoh.txt"

    # Lokasi penyimpanan laporan
    path_laporan = "output/laporan_nilai.txt"

    # Input KKM
    while True:
        try:
            kkm = float(input("Masukkan nilai KKM: "))

            if 0 <= kkm <= 100:
                break
            else:
                print("KKM harus berada pada rentang 0-100.")

        except ValueError:
            print("Input harus berupa angka.")

    # Membaca data mahasiswa
    data = baca_data(path_data)

    # Memeriksa apakah data tersedia
    if len(data) == 0:
        print("\nTidak ada data valid untuk dianalisis.")
        return

    # Menampilkan data mahasiswa
    tampilkan_data(data)

    # Menghitung statistik
    statistik = hitung_statistik(data)

    # Menghitung ketuntasan
    ketuntasan = hitung_ketuntasan(data, kkm)

    # Membuat laporan
    laporan = buat_laporan(
        data,
        statistik,
        ketuntasan,
        kkm
    )

    # Menampilkan laporan
    print("\n")
    print(laporan)

    # Menyimpan laporan
    simpan_laporan(laporan, path_laporan)

    print("\nProgram selesai.")


if __name__ == "__main__":
    main()
