for i in range(1,5,1):
    for j in range(0,3,1):
        print(i*j, end="")
    print ()

print("\n")
baris = int(input('tentukan baris dari segitiga: '))
for i in range(1,baris+1):
    for j in range(1,i+1):
        print('*', end=" ")
    print()