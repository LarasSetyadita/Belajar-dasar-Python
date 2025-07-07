text = str(input("Masukkan teks: "))

for i in range(1, len(text), 2):
    temp = text
    text = temp[: i] + "*" + temp[i + 1:]

print(text)