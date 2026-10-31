
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from src.data_io import baca_data, simpan_laporan


def test_baca_data_normal():
    path = ROOT_DIR / "data" / "nilai_contoh.txt"

    data = baca_data(path)

    assert len(data) == 8
    assert data[0]["nama"] == "Ayu"
    assert data[0]["nilai"] == 85

    print("TC01: Membaca data normal - LULUS")


def test_file_tidak_ditemukan():
    with TemporaryDirectory() as folder:
        path = Path(folder) / "file_tidak_ada.txt"

        data = baca_data(path)

        assert data == []

    print("TC02: File tidak ditemukan - LULUS")


def test_file_kosong():
    with TemporaryDirectory() as folder:
        path = Path(folder) / "data_kosong.txt"
        path.write_text("", encoding="utf-8")

        data = baca_data(path)

        assert data == []

    print("TC03: File kosong - LULUS")


def test_data_invalid():
    with TemporaryDirectory() as folder:
        path = Path(folder) / "data_invalid.txt"

        path.write_text(
            "Ayu,85\n"
            "Budi,abc\n"
            ",90\n"
            "Citra,120\n"
            "Dina,70,80\n"
            "Eko,75\n",
            encoding="utf-8"
        )

        data = baca_data(path)

        assert len(data) == 2
        assert data[0]["nama"] == "Ayu"
        assert data[1]["nama"] == "Eko"

    print("TC04: Data invalid - LULUS")


def test_simpan_laporan():
    with TemporaryDirectory() as folder:
        path = Path(folder) / "output" / "test_laporan.txt"

        isi = "Pengujian laporan berhasil."

        hasil_simpan = simpan_laporan(isi, path)

        assert hasil_simpan is True
        assert path.exists()

        hasil_baca = path.read_text(encoding="utf-8")

        assert hasil_baca == isi

    print("TC05: Menyimpan laporan - LULUS")


if __name__ == "__main__":
    test_baca_data_normal()
    test_file_tidak_ditemukan()
    test_file_kosong()
    test_data_invalid()
    test_simpan_laporan()

    print("\nSemua pengujian data I/O berhasil!")
