def get_biaya(nim):
    if len(nim) < 4:
        return 0  # Biaya tidak valid
    kode_jurusan = nim[2:4]  # Ambil karakter ke-3 dan ke-4
    if kode_jurusan == "11":
        return 9600000  # Biaya Teknik Informatika
    elif kode_jurusan == "12":
        return 9100000  # Biaya Sistem Informasi
    elif kode_jurusan == "13":
        return 9300000  # Biaya Sistem Komputer
    else:
        return 0  # Kode jurusan tidak valid
