import sys
from pathlib import Path

# Menambahkan folder utama proyek ke jalur pencarian Python
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from src.analisis import (
    validasi_nilai,
    hitung_statistik,
    tentukan_status,
    hitung_ketuntasan
)


def test_nilai_valid():
    assert validasi_nilai(0)
    assert validasi_nilai(100)
    assert validasi_nilai(80)


def test_nilai_invalid():
    assert not validasi_nilai(105)
    assert not validasi_nilai(-5)
    assert not validasi_nilai("abc")
    assert not validasi_nilai(True)


def test_hitung_statistik():
    data = [
        {"nama": "Ayu", "nilai": 80},
        {"nama": "Budi", "nilai": 70},
        {"nama": "Citra", "nilai": 90}
    ]

    hasil = hitung_statistik(data)

    assert hasil["jumlah"] == 3
    assert hasil["rata_rata"] == 80
    assert hasil["minimum"] == 70
    assert hasil["maksimum"] == 90


def test_statistik_data_kosong():
    hasil = hitung_statistik([])

    assert hasil is None


def test_tentukan_status():
    assert tentukan_status(80, 75) == "Tuntas"
    assert tentukan_status(70, 75) == "Belum Tuntas"


def test_batas_kkm():
    assert tentukan_status(75, 75) == "Tuntas"


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
    test_statistik_data_kosong()
    test_tentukan_status()
    test_batas_kkm()
    test_hitung_ketuntasan()

    print("Semua pengujian analisis berhasil!")
