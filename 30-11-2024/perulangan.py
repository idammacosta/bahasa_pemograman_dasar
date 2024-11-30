number_list = []
n = int(input("Input ukuran List: "))
jum = 0
print("\n")
for i in range(0,n):
    print("Input nilai pada indeks ke-:",i)
    list_item = int(input())
    jum = jum+list_item
    number_list.append(list_item)


print("Data List: ",number_list)
print("Jumlah: ",jum)