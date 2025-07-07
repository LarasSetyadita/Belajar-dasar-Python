"""
Question:
Buatlah skrip yang membaca bilangan bulat dari papan-ketik. Sebagai contoh, bilangan yang dimasukkan adalah 203.
Maka tampilannya berupa:
*******203
Jika bilangan yang dimasukkan 12345, tampilannya berupa:
*****12345

"""
data = int (input('Masukkan sebuah bilangan: '))
print(str(data).rjust(9, '*'))