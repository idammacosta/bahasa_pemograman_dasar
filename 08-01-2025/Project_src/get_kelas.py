def get_kelas(nim):
    if len(nim) < 6:
        return "NIM tidak valid (kurang dari 6 karakter)"
    kode_kelas = nim[5]  # Ambil karakter ke-6
    if kode_kelas == "0":
        return "Reguler"
    elif kode_kelas == "1":
        return "Karyawan"
    else:
        return "Kode kelas tidak valid"
