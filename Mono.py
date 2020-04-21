from string import printable
from random import shuffle

keys = list(printable)
shuffle_keys = list(printable)
shuffle(shuffle_keys)

maps = dict(zip(keys,shuffle_keys))
reverse_map = dict(zip(shuffle_keys,keys))

def encrypt(message):
    cipher = []
    for letters in message:
        cipherletters = maps[letters]
        cipher.append(cipherletters)
    return "".join(cipher)

def decrypt(cipher):
    plaintext=[]
    for letters in cipher:
        plain =reverse_map[letters]
        plaintext.append(plain)
    return "".join(plaintext)


a=input("Enter A Plain Text ")
print("The Cipher Text is ",encrypt(a))
print("The PlainText of the cipher ",decrypt(encrypt(a)))







    





