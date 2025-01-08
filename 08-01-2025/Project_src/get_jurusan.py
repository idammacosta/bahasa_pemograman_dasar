def get_jurusan(nim):
    if len(nim) < 4:
        return "NIM tidak valid (kurang dari 4 karakter)"
    kode_jurusan = nim[2:4]  # Ambil karakter ke-3 dan ke-4
    if kode_jurusan == "11":
        return "Teknik Informatika"
    elif kode_jurusan == "12":
        return "Sistem Informasi"
    elif kode_jurusan == "13":
        return "Sistem Komputer"
    else:
        return "Kode jurusan tidak valid"
