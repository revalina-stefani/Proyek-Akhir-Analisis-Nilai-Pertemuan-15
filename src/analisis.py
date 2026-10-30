
def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berada
    dalam rentang 0 sampai 100.
    """
    if nilai >= 0 and nilai <= 100:
        return True
    else:
        return False


def hitung_statistik(data):
    """
    Menghitung rata-rata, nilai minimum,
    dan nilai maksimum.
    """

    if len(data) == 0:
        return None

    daftar_nilai = []

    for mahasiswa in data:
        daftar_nilai.append(mahasiswa["nilai"])

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    nilai_minimum = min(daftar_nilai)
    nilai_maksimum = max(daftar_nilai)

    statistik = {
        "rata_rata": rata_rata,
        "minimum": nilai_minimum,
        "maksimum": nilai_maksimum
    }

    return statistik


def tentukan_status(nilai, kkm):
    """
    Menentukan status ketuntasan mahasiswa.
    """

    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Belum Tuntas"


def hitung_ketuntasan(data, kkm):
    """
    Menghitung jumlah mahasiswa yang tuntas
    dan belum tuntas.
    """

    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for mahasiswa in data:
        status = tentukan_status(
            mahasiswa["nilai"], kkm
        )

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    hasil = {
        "tuntas": jumlah_tuntas,
        "belum_tuntas": jumlah_belum_tuntas
    }

    return hasil
