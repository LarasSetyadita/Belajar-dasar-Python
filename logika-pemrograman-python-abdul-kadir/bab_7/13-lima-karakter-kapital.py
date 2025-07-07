text = str(input('Masukkan teks disini : '))
temp = text
text_up = text.upper()

text = text_up[: 5] + temp[5:]
print(text)