n = int (input('masukkan input bilangan bulat minimal 1:'))

for i in range (0, n):

    # kode untuk persegi sebelah kiri
    if i == 0 or i == n-1:
        for k in range (0, n):
            print('*', end='')
    else : 
        print('*', end='')
        for k in range (0, n-2):
            print(' ', end='')
        print('*', end='')

    # spasi pemisah
    print(' ', end='') 

    # kode untuk persegi sebelah kanan
    for j in range (0, n):
        print('*', end='')

    print()