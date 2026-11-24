undangan = set()
webinar_a = set()
webinar_b = set()

try:
    undangan.update(map(str.strip, input("Masukkan daftar undangan (pisahkan dengan koma): ").split(",")))
    undangan.discard("")

    webinar_a.update(map(str.strip, input("Masukkan peserta Webinar A (pisahkan dengan koma): ").split(",")))
    webinar_a.discard("")

    webinar_b.update(map(str.strip, input("Masukkan peserta Webinar B (pisahkan dengan koma): ").split(",")))
    webinar_b.discard("")

    semua_peserta = webinar_a | webinar_b
    hadir_keduanya = webinar_a & webinar_b
    hanya_satu = webinar_a ^ webinar_b
    tidak_hadir = undangan - semua_peserta

    print("\n=== HASIL ANALISIS WEBINAR ===")
    print("Semua peserta kedua webinar:", ", ".join(sorted(semua_peserta)) if semua_peserta else "-")
    print("Hadir di kedua webinar:", ", ".join(sorted(hadir_keduanya)) if hadir_keduanya else "-")
    print("Hanya hadir di satu webinar:", ", ".join(sorted(hanya_satu)) if hanya_satu else "-")
    print("Undangan yang tidak hadir:", ", ".join(sorted(tidak_hadir)) if tidak_hadir else "-")
except ValueError as e:
    print(f"Terjadi kesalahan input: {e}")
