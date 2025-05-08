jumlah_pembelian = int (input('Masukkan jumlah pembelian barang: '))

if jumlah_pembelian < 6 :
    harga_per_unit = 78000
elif jumlah_pembelian < 13:
    harga_per_unit = 75000
elif jumlah_pembelian < 21:
    harga_per_unit = 72000
elif jumlah_pembelian < 41:
    harga_per_unit = 68000
elif jumlah_pembelian < 100:
    harga_per_unit = 65000
else :
    harga_per_unit = 58000

harga_total = jumlah_pembelian * harga_per_unit
print('harga yang harus dibayarkan adalah :', harga_total)