
BATAS_NILAI_MINIMUM = 0
BATAS_NILAI_MAKSIMUM = 100


def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berupa angka
    dan berada dalam rentang 0 sampai 100.
    """
    if isinstance(nilai, bool):
        return False

    if not isinstance(nilai, (int, float)):
        return False

    return BATAS_NILAI_MINIMUM <= nilai <= BATAS_NILAI_MAKSIMUM


def hitung_statistik(data):
    """
    Menghitung rata-rata, nilai minimum,
    dan nilai maksimum.
    """
    if not data:
        return None

    daftar_nilai = [mahasiswa["nilai"] for mahasiswa in data]

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)

    return {
        "jumlah": len(daftar_nilai),
        "rata_rata": rata_rata,
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai)
    }


def tentukan_status(nilai, kkm):
    """
    Menentukan status ketuntasan mahasiswa.
    """
    if nilai >= kkm:
        return "Tuntas"

    return "Belum Tuntas"


def hitung_ketuntasan(data, kkm):
    """
    Menghitung jumlah mahasiswa yang tuntas
    dan belum tuntas.
    """
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for mahasiswa in data:
        status = tentukan_status(mahasiswa["nilai"], kkm)

        if status == "Tuntas":
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    return {
        "tuntas": jumlah_tuntas,
        "belum_tuntas": jumlah_belum_tuntas
    }
