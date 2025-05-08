bil1 = int (input('masukkan bilangan pertama: '))
bil2 = int (input('masukkan bilangan kedua: '))
bil3 = int (input('masukkan bilangan ketiga: '))

while bil1 == bil2 or bil2 == bil3 or bil1 == bil3:
    print('tidak boleh ada bilangan yang sama')
    bil1 = int (input('masukkan bilangan pertama: '))
    bil2 = int (input('masukkan bilangan kedua: '))
    bil3 = int (input('masukkan bilangan ketiga: '))

print('bilangan pertama: %d, bilangan kedua: %d, bilangan ketiga: %d' % (bil1, bil2, bil3))