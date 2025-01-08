def get_biaya(nim):

    kode_biaya = int(nim[10])
    if kode_biaya == 1:
        return "9.600.000"
    elif kode_biaya == 2:
        return "9.100.000"
    elif kode_biaya == 3:
        return "9.300.000"
    else:
        return "Biaya tidak diketahui"
