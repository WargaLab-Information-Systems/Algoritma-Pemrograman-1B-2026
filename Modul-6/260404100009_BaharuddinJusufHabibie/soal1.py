batasAkhir = "selesai"
namaTerlarang = "admin"
panjangMinimal = 4


def kumpulkan_nama():
    # Meminta nama berulang kali sampai pengguna mengetik 'selesai' (persis).
    daftar = []
    while True:
        nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
        if nama == batasAkhir:
            break
        daftar.append(nama)
    return daftar


def evaluasi_nama(daftar):
    # Memeriksa daftar dari awal hingga akhir dan menandai nama yang tidak valid.
    for nama in daftar:
        if nama == namaTerlarang or len(nama) < panjangMinimal:
            print(f'Nama "{nama}" tidak valid.')


def hapus_penyusup(daftar):
    # Menghapus kemunculan pertama nama penyusup; tidak crash bila tidak ditemukan.
    penyusup = input("Ketik nama yang dicurigai sebagai penyusup: ")
    try:
        daftar.remove(penyusup)
        print(f'Nama "{penyusup}" berhasil dihapus dari pendaftaran.')
    except ValueError:
        print(f'Nama "{penyusup}" tidak ditemukan di dalam pendaftaran.')


def proses_pendaftaran_klub():
    daftar = kumpulkan_nama()
    evaluasi_nama(daftar)
    hapus_penyusup(daftar)
    print("Daftar anggota akhir:", daftar)


proses_pendaftaran_klub()