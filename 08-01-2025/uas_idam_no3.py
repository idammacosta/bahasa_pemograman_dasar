def f(x):
    if x == 0:  
        return "f(x) tidak terdefinisi untuk x = 0"
    return 2 * x**3 + 2 * x + 15 / x

try:
    x = int(input("Masukkan nilai x: "))
    hasil = f(x)
    print(f"f({x}) = {hasil}")
except ValueError:
    print("Hanya bisa memasukkan bilangan Bulat.")