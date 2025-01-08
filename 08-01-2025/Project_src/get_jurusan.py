def get_jurusan(nim):

    kode_jurusan = int(nim[11])
    if kode_jurusan == 2:
        return "Teknik Informatika"
    elif kode_jurusan == 3:
        return "Sistem Informasi"
    elif kode_jurusan == 5:
        return "Sistem Komputer"
    else:
        return "Jurusan tidak dikenal"
