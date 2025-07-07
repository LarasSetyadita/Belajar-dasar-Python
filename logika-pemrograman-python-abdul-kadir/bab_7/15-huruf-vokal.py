text = str(input("Masukkan teks : "))

vokal = 'aiueo'
total = 0

for i in text:
    if i.lower() in vokal:
        total +=1

print(total)