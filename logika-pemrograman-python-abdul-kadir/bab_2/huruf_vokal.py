huruf = str (input('masukkan 1 huruf: '))
input_lower = huruf.lower()

if input_lower == 'a' or input_lower =='i' or input_lower =='u' or input_lower =='e' or input_lower=='o':
    print("%s adalah huruf vokal"% huruf)

else :
    print("%s bukan huruf vokal"% huruf)