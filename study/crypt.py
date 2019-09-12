from simplecrypt import encrypt, decrypt, DecryptionException

passwords = []
encrypted = ''
with open('passwords.txt') as inData:
    passwords += inData.read().split('\n')

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
'''
for pas in passwords:
    for cr in crypted:
        print(cr)
        uncrypted += decrypt(pas,crypted)
    print(uncrypted)
'''

for p in passwords:
    try:
        s = decrypt(p, encrypted)
    except DecryptionException:
        pass
    else:
        print(p, s)
#with open('encrypted.bin','rb') as inData:
#    crypted = inData.read()
#    print(crypted)
    #print(inData.read())
    #print(decrypt((inData.read()),passwords[0]))

print(passwords)