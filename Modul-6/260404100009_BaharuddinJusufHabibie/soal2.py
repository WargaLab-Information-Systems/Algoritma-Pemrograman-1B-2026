batasAkhir = "cukup"

def kumpulkanKeTuple(prompt):
    # Mengumpulkan input berulang sampai 'cukup', lalu mengunci hasilnya sebagai tuple.
    sementara = []
    while True:
        nilai = input(prompt)
        if nilai.strip().lower() == batasAkhir:
            break
        sementara.append(nilai)
    return tuple(sementara)


def susunJadwalShift():
    # Tahap 1: asisten awal, dikunci (tuple)
    asistenAwal = kumpulkanKeTuple("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")

    # Tahap 2: asisten tambahan, digabung ke tuple baru (tuple tidak diubah, dibuat baru)
    asistenTambahan = input("Masukkan nama asisten tambahan yang mendadak bergabung: ")
    asistenAkhir = asistenAwal + (asistenTambahan,)

    # Tahap 3: hari tugas, dikunci (tuple)
    hariTugas = kumpulkanKeTuple("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")

    # Pengecualian
    asistenKecuali = input("Masukkan nama asisten yang dikecualikan: ").strip().lower()
    hariKecuali = input("Masukkan hari pengecualiannya: ").strip().lower()

    # Pasangkan setiap asisten dengan setiap hari, lewati kombinasi pengecualian
    jumlah = 0
    print("\nDaftar kombinasi shift:")
    for asisten in asistenAkhir:
        for hari in hariTugas:
            if asisten.strip().lower() == asistenKecuali and hari.strip().lower() == hariKecuali:
                continue
            print(f"- {asisten} bertugas pada hari {hari}")
            jumlah += 1

    if jumlah == 0:
        print("Tidak ada kombinasi shift yang berhasil dibuat.")


susunJadwalShift()