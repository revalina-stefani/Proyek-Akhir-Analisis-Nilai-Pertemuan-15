
from pathlib import Path

from .data_io import baca_data, simpan_laporan
from .analisis import (
    hitung_statistik,
    hitung_ketuntasan
)
from .utilitas import (
    tampilkan_judul,
    tampilkan_data,
    buat_laporan
)


# Konfigurasi program
KKM_DEFAULT = 75

FOLDER_PROYEK = Path(__file__).resolve().parent.parent

PATH_DATA = FOLDER_PROYEK / "data" / "nilai_contoh.txt"
PATH_LAPORAN = FOLDER_PROYEK / "output" / "laporan_nilai.txt"


def main():
    tampilkan_judul()

    # Input KKM
    while True:
        try:
            kkm = float(
                input(f"Masukkan nilai KKM [{KKM_DEFAULT}]: ")
                or KKM_DEFAULT
            )

            if 0 <= kkm <= 100:
                break

            print("KKM harus berada pada rentang 0-100.")

        except ValueError:
            print("Input harus berupa angka.")

    # Membaca data mahasiswa
    data = baca_data(PATH_DATA)

    # Memeriksa ketersediaan data
    if not data:
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
    simpan_laporan(laporan, PATH_LAPORAN)

    print("\nProgram selesai.")


if __name__ == "__main__":
    main()
