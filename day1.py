
decimal = 10 # value = 10
hexadecimal = 0x10 # value = 16
binary = 0b1011010 # value = 90

unicodeString = 'caf£'
byteString = b'caf\xc2\xa3'
print(unicodeString.encode('utf-8'))
print(byteString.decode('utf-8'))


val = -0

if val % 2 is 0:
    print('Even')
else:
    print('Odd') 