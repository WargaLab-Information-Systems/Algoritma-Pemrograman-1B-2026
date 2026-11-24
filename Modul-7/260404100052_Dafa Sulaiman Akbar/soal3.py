undangan = set()
webinar_a = set()
webinar_b = set()


def isi_set(himpunan, judul):
    print("\nMasukkan nama", judul, "(ketik 'selesai' untuk berhenti)")
    while True:
        nama = input("Nama: ").strip().title()
        if nama.lower() == "selesai":
            break
        if nama != "":
            himpunan.add(nama)


isi_set(undangan, "undangan")
isi_set(webinar_a, "peserta Webinar A")
isi_set(webinar_b, "peserta Webinar B")

semua_peserta = webinar_a | webinar_b
hadir_keduanya = webinar_a & webinar_b
hanya_satu = webinar_a ^ webinar_b
tidak_hadir = undangan - (webinar_a | webinar_b)

print("\n=== HASIL ===")
print("Semua peserta kedua webinar :", ", ".join(sorted(semua_peserta)) or "-")
print("Hadir di kedua webinar      :", ", ".join(sorted(hadir_keduanya)) or "-")
print("Hanya hadir di satu webinar :", ", ".join(sorted(hanya_satu)) or "-")
print("Undangan tidak hadir        :", ", ".join(sorted(tidak_hadir)) or "-")