print("       DEC       OCT       HEX")
print("------------------------------")

oct = ('0', '1', '2', '3', '4', '5', '6', '7')
hex = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

for i in range(64):
    # print bilangan desimal
    print(str(i).rjust(10, " "), end="")

    # print bilangan oktal
    o = int(i)
    octstr = str(oct[int(o % 8)])
    o = int(o / 8)
    while o > 0:
        octstr = octstr + oct[int(o % 8)]
        o = int(o / 8)
    print(octstr.rjust(10, " "), end="")

    # print bilangan hexadesimal
    h = int(i)
    hexstr = str(hex[int(h % 16)])
    h = int(h / 16)
    while h > 0:
        hexstr = hexstr + hex[int(h % 16)]
        h = int(h / 16)
    print(hexstr.rjust(10, " "))

#print("\n")
