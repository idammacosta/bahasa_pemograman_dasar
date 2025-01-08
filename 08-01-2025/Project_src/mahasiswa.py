from pendaftaran import cetak_kwitansi
from get_jurusan import get_jurusan
from get_kelas import get_kelas
from get_biaya import get_biaya

def main():
    nim = input("Masukkan NIM: ")
    if len(nim) < 6:
        print("Error: NIM harus memiliki minimal 6 karakter.")
        return

    nama = input("Masukkan Nama: ")
    no_hp = input("Masukkan No. HP: ")
    email = input("Masukkan Email: ")
    alamat = input("Masukkan Alamat: ")

    jurusan = get_jurusan(nim)
    kelas = get_kelas(nim)
    biaya = get_biaya(nim)

    cetak_kwitansi(nim, nama, no_hp, email, alamat)
    print(f"Jurusan   : {jurusan}")
    print(f"Kelas     : {kelas}")
    print(f"Biaya     : Rp {biaya:,}")

if __name__ == "__main__":
    main()
