try:
    harga1 = int(input("Masukkan harga pertama: "))
    harga2 = int(input("Masukkan harga kedua: "))
    harga3 = int(input("Masukkan harga ketiga: "))
    
    harga = [harga1, harga2, harga3]
    
    harga.sort()

    nilai_tengah = harga[1]

    print(f"Harga tengah (bukan tertinggi atau terendah): {nilai_tengah}")
except ValueError:
    print("Masukkan bilangan bulat saja.")
