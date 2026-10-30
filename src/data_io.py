
def baca_data(path):
    """
    Membaca data mahasiswa dari file teks.
    Format: nama,nilai
    """

    data = []

    try:
        with open(path, "r") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        print(f"Baris {nomor_baris} tidak valid.")
                        continue

                    nama = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    if not nama:
                        print(f"Nama pada baris {nomor_baris} kosong.")
                        continue

                    if 0 <= nilai <= 100:
                        mahasiswa = {
                            "nama": nama,
                            "nilai": nilai
                        }

                        data.append(mahasiswa)
                    else:
                        print(f"Nilai {nama} di luar rentang 0-100.")

                except ValueError:
                    print(f"Data pada baris {nomor_baris} tidak valid.")

    except FileNotFoundError:
        print("Error: File data tidak ditemukan.")

    return data


def simpan_laporan(isi_laporan, path):
    """
    Menyimpan laporan hasil analisis ke file teks.
    """

    try:
        with open(path, "w") as file:
            file.write(isi_laporan)

        print(f"Laporan berhasil disimpan di {path}")

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
