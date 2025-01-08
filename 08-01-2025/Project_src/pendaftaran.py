from get_jurusan import get_jurusan
from get_kelas import get_kelas
from get_biaya import get_biaya

def cetak_kwitansi(nim, nama, no_hp, email, alamat):
    jurusan = get_jurusan(nim)
    kelas = get_kelas(nim)
    biaya = get_biaya(nim)

    kwitansi = f"""
    ============================
    KWITANSI PENDAFTARAN
    ============================
    NIM     : {nim}
    Nama    : {nama}
    No. HP  : {no_hp}
    Email   : {email}
    Alamat  : {alamat}

    Jurusan : {jurusan}
    Kelas   : {kelas}
    Biaya   : Rp {biaya}
    ============================
    """
    print(kwitansi)

# Contoh penggunaan
if __name__ == "__main__":
    nim = "2411502025"
    nama = "Idam Machosta"
    no_hp = "081234567890"
    email = "idam@example.com"
    alamat = "Jl. Merdeka No. 1"
    cetak_kwitansi(nim, nama, no_hp, email, alamat)
