text = str(input('Masukkan teks : '))

for i in range(len(text)):
    character = str(text[i])
    if (character not in text[i + 1:]):
        print(character)
        break
