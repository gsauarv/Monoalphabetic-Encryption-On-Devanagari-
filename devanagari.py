from random import shuffle
chars=["क","ख","ग","घ","ङ","च","छ","ज","झ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","व","स","श","ष","ह","ञ"]
symbols=["ै","ौ","ृ","ु","ू","ि","ी","ो","ा","े"]

#maps for chars
keys=list(chars)
shuffled_keys=list(chars)
shuffle(shuffled_keys)

#Maps for Symbols
keys_symbols=list(symbols)
shuffled_keys_symbols=list(symbols)
shuffle(shuffled_keys_symbols)

#dict for maps
maps=dict(zip(keys,shuffled_keys))
reversed_maps=dict(zip(shuffled_keys,keys))

#dict for symbols maps
maps_symbols=dict(zip(keys_symbols,shuffled_keys_symbols))
reversed_maps_symbols=dict(zip(shuffled_keys_symbols,keys_symbols))

def encrypt(message):
    cipher=[]    
    for letters in message:
        if letters in chars:
            cipher_letters=maps[letters]
            cipher.append(cipher_letters)
        elif letters in symbols:
            cipher_symbols=maps_symbols[letters]
            cipher.append(cipher_symbols)
    
    return "".join(cipher)


def decrypt(ciphers):
    plaintext=[]
    for letters in ciphers:
        if letters in chars:
            plaintext_letters=reversed_maps[letters]
            plaintext.append(plaintext_letters)
        elif letters in symbols:
            plaintext_symbols=reversed_maps_symbols[letters]
            plaintext.append(plaintext_symbols)
            
    return " ".join(plaintext)


a=encrypt("मेरोदेशनेपालहो")
print("Encrypted Letters is: ",a)
b=decrypt(a)
print("Decrypted Letters is:",b)
