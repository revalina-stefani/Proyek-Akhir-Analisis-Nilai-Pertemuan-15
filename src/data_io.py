
from pathlib import Path


def baca_data(path):
    """
    Membaca data mahasiswa dari file teks.
    Format: nama,nilai
    """

    data = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor_baris} tidak valid.")
                    continue

                nama = bagian[0].strip()

                if not nama:
                    print(f"Nama pada baris {nomor_baris} kosong.")
                    continue

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} bukan angka.")
                    continue

                if 0 <= nilai <= 100:
                    data.append({
                        "nama": nama,
                        "nilai": nilai
                    })
                else:
                    print(
                        f"Nilai {nama} di luar rentang 0-100."
                    )

    except FileNotFoundError:
        print(f"Error: File {path} tidak ditemukan.")

    except OSError as error:
        print(f"Gagal membaca file: {error}")

    return data


def simpan_laporan(isi_laporan, path):
    """
    Menyimpan laporan hasil analisis ke file teks.
    """

    try:
        lokasi_file = Path(path)

        lokasi_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            lokasi_file,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(isi_laporan)

        print(f"Laporan berhasil disimpan di {lokasi_file}")

        return True

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
