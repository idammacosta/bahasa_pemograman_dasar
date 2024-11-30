baris = int(input('Tentukan jumlah baris dari segitiga: '))
angka = 1 

for i in range(1, baris + 1): 
    print(' ' * (baris - i), end="")  
    for j in range(1, i + 1):
        print(angka, end=" ")
        angka += 1
    print()