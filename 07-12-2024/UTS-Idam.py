from datetime import datetime

# Daftar harga menu
menu = {
    "Latte": 25000,
    "Cappuccino": 23000,
    "Americano": 20000,
    "Milk Tea": 21000
}

# Variabel untuk melacak jumlah pelanggan
pelanggan_ke = 0

def tampilkan_menu():
    print("\n--- Menu Cafetaria ---")
    for item, harga in menu.items():
        print(f"{item} : Rp {harga:,}")
    print("----------------------")

def hitung_diskon(total, pelanggan_ke, waktu_pesan):
    diskon = 0
    
    # Diskon 30% untuk 10 pelanggan pertama
    if pelanggan_ke <= 10:
        diskon += 0.30
    
    # Diskon 20% jika pemesanan antara 07:00 - 08:00 WIB
    if waktu_pesan.hour == 7:
        diskon += 0.20
    
    # Menghitung total setelah diskon
    total_diskon = total * diskon
    total_bayar = total - total_diskon
    
    return total_bayar, total_diskon

def main():
    global pelanggan_ke
    
    # Input waktu pemesanan
    waktu_input = input("\nMasukkan waktu pemesanan (HH:MM, 24 jam format): ")
    
    try:
        waktu_pesan = datetime.strptime(waktu_input, "%H:%M").time()
    except ValueError:
        print("Format waktu salah. Gunakan format HH:MM.")
        return
    
    # Cek jam operasional
    if not (7 <= waktu_pesan.hour < 21):
        print("Maaf, pemesanan hanya dapat dilakukan antara pukul 07:00 hingga 21:00 WIB.")
        return
    
    # Tampilkan menu
    tampilkan_menu()
    
    # Input pesanan
    menu_pilihan = input("Pilih menu (Latte, Cappuccino, Americano, Milk Tea): ")
    if menu_pilihan not in menu:
        print("Menu tidak tersedia. Silakan pilih menu yang benar.")
        return
    
    try:
        jumlah = int(input(f"Masukkan jumlah {menu_pilihan}: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return
    
    # Proses pesanan
    pelanggan_ke += 1
    harga_satuan = menu[menu_pilihan]
    total_harga = harga_satuan * jumlah
    total_bayar, total_diskon = hitung_diskon(total_harga, pelanggan_ke, waktu_pesan)
    
    # Tampilkan hasil
    print("\n--- Rincian Pembayaran ---")
    print(f"Menu        : {menu_pilihan}")
    print(f"Jumlah      : {jumlah}")
    print(f"Harga Total : Rp {total_harga:,}")
    print(f"Diskon      : Rp {total_diskon:,}")
    print(f"Total Bayar : Rp {total_bayar:,}")
    print("----------------------------")

        
if __name__ == "__main__":
    main()
