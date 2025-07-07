n = int (input('masukkan bilangan bulat minimal 1: '))

for i in range (0, 5):
    for j in range (0, n-i):
        print(' ', end='')

    for j in range (0,n*2):
        print('*', end='')
    
    print('\n')