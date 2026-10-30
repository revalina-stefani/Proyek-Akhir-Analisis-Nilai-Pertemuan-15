
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.data_io import baca_data, simpan_laporan


def test_baca_data_normal():
    data = baca_data("data/nilai_contoh.txt")

    assert len(data) == 8
    assert data[0]["nama"] == "Ayu"
    assert data[0]["nilai"] == 85

    print("TC01: Membaca data normal - LULUS")


def test_file_tidak_ditemukan():
    data = baca_data("data/file_tidak_ada.txt")

    assert data == []

    print("TC05: File tidak ditemukan - LULUS")


def test_file_kosong():
    path = "data/data_kosong.txt"

    with open(path, "w") as file:
        file.write("")

    data = baca_data(path)

    assert data == []

    os.remove(path)

    print("TC07: File kosong - LULUS")


def test_simpan_laporan():
    path = "output/test_laporan.txt"

    isi = "Pengujian laporan berhasil."

    simpan_laporan(isi, path)

    with open(path, "r") as file:
        hasil = file.read()

    assert hasil == isi

    os.remove(path)

    print("Pengujian penyimpanan laporan - LULUS")


if __name__ == "__main__":
    test_baca_data_normal()
    test_file_tidak_ditemukan()
    test_file_kosong()
    test_simpan_laporan()

    print("\nSemua pengujian data I/O selesai!")
