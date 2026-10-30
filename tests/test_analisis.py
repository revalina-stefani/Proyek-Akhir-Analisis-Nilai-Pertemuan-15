
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.analisis import (
    validasi_nilai,
    hitung_statistik,
    tentukan_status,
    hitung_ketuntasan
)


def test_nilai_valid():
    assert validasi_nilai(0) == True
    assert validasi_nilai(100) == True
    assert validasi_nilai(80) == True


def test_nilai_invalid():
    assert validasi_nilai(105) == False
    assert validasi_nilai(-5) == False


def test_hitung_statistik():
    data = [
        {"nama": "Ayu", "nilai": 80},
        {"nama": "Budi", "nilai": 70},
        {"nama": "Citra", "nilai": 90}
    ]

    hasil = hitung_statistik(data)

    assert hasil["rata_rata"] == 80
    assert hasil["minimum"] == 70
    assert hasil["maksimum"] == 90


def test_tentukan_status():
    assert tentukan_status(80, 75) == "Tuntas"
    assert tentukan_status(70, 75) == "Belum Tuntas"


def test_hitung_ketuntasan():
    data = [
        {"nama": "Ayu", "nilai": 80},
        {"nama": "Budi", "nilai": 70},
        {"nama": "Citra", "nilai": 90}
    ]

    hasil = hitung_ketuntasan(data, 75)

    assert hasil["tuntas"] == 2
    assert hasil["belum_tuntas"] == 1


if __name__ == "__main__":
    test_nilai_valid()
    test_nilai_invalid()
    test_hitung_statistik()
    test_tentukan_status()
    test_hitung_ketuntasan()

    print("Semua pengujian berhasil!")
