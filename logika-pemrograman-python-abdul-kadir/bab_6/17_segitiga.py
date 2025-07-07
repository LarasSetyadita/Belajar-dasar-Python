n = int(input("Masukkan bilangan bulat antara 3-9: "))
while(n < 3 or n > 9) :
    n = int(input("Input anda tidak diantara 3-9, masukkan angka yang benar: "))

for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end="")
    for k in range(1, 2 * (n - i) + 2):
        print(n, end="")
    print()