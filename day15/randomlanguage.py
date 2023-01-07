import random
import string
text = input("Enter text for encrypt decrypt:  ")
print("Generating....")
print("............. encrypt text ...........")
# encrypt
en=''
if(len(text)<=3):
    text = text [::-1]
    print(text)
else:
    for i in range(1,len(text)):
        en+=text[i]
    en+=text[0]
    enc = ''.join(random.choice(string.ascii_letters) for x in range(3))
    enc+=en
    print(enc)

print("............. decrypt text ...........")
# decrypt
dec=""
decrypt=""
if(len(en)<=3):
    text = text [::-1]
    print(text)
else:
    for i in range(3, len(enc)-1):
        dec+=enc[i]
    decrypt = enc[len(enc)-1]
    decrypt+=dec
    print(decrypt)