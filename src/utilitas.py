
def tampilkan_judul():
    print("=" * 45)
    print(" PROGRAM REKAP DAN ANALISIS NILAI")
    print("       MATEMATIKA KELAS")
    print("=" * 45)


def tampilkan_data(data):
    print("\nDAFTAR NILAI MAHASISWA")
    print("-" * 45)
    print(f"{'No':<5}{'Nama':<20}{'Nilai':<10}")
    print("-" * 45)

    for nomor, mahasiswa in enumerate(data, start=1):
        print(
            f"{nomor:<5}"
            f"{mahasiswa['nama']:<20}"
            f"{mahasiswa['nilai']:<10.2f}"
        )

    print("-" * 45)


def buat_laporan(data, statistik, ketuntasan, kkm):
    """
    Membuat teks laporan hasil analisis.
    """

    laporan = []

    laporan.append("=" * 45)
    laporan.append("LAPORAN ANALISIS NILAI MATEMATIKA")
    laporan.append("=" * 45)

    laporan.append("\nDAFTAR NILAI MAHASISWA")

    for nomor, mahasiswa in enumerate(data, start=1):
        status = (
            "Tuntas"
            if mahasiswa["nilai"] >= kkm
            else "Belum Tuntas"
        )

        laporan.append(
            f"{nomor}. {mahasiswa['nama']} - "
            f"{mahasiswa['nilai']:.2f} - {status}"
        )

    laporan.append("\nSTATISTIK NILAI")
    laporan.append(f"Rata-rata : {statistik['rata_rata']:.2f}")
    laporan.append(f"Minimum   : {statistik['minimum']:.2f}")
    laporan.append(f"Maksimum  : {statistik['maksimum']:.2f}")

    laporan.append("\nKETUNTASAN")
    laporan.append(f"KKM             : {kkm}")
    laporan.append(f"Jumlah Tuntas   : {ketuntasan['tuntas']}")
    laporan.append(
        f"Jumlah Belum Tuntas : "
        f"{ketuntasan['belum_tuntas']}"
    )

    laporan.append("=" * 45)

    return "\n".join(laporan)
