"""
Question:
 Selama masa promosi, swalayan Megatama memberikan diskon sebesar 10%. Buatlah skrip yang meminta total pembelian
 yang dimasukkan dari papan-ketik. Kemudian, skrop melaporkan total pembelian, besar diskon, dan total pembayaran.
"""
harga = float (input('masukkan harga barang: '))
diskon = 0.1
harga_diskon = harga * diskon
harga_bayar = harga - harga_diskon

print('harga barang: ', harga)
print('harga diskon', harga_diskon)
print('Nilai yang harus dibayarkan', harga_bayar)