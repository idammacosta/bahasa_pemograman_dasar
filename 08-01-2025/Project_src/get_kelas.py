def get_kelas(nim):

    kode_kelas = int(nim[12])
    if kode_kelas == 0:
        return "Reguler"
    elif kode_kelas == 1:
        return "Karyawan"
    else:
        return "Kelas tidak dikenal"
