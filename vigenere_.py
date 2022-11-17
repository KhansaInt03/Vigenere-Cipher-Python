from ordo import *

ord_dict = ascii_to_ordo()

def vigenere_encrypt():

    plaintext = input('Your Plaintext:\n>>')
    key = input('Your Key:\n>>')

    plaintext_ord = [ v for letter in plaintext for k,v in ord_dict.items() if letter == k ]
    key_ord = [ v for letter in key for k,v in ord_dict.items() if letter == k ]

    if len(plaintext_ord) != len(key_ord):
        if len(plaintext_ord) < len(key_ord):
            add = len(key_ord) - len(plaintext_ord)
            for i in range(add):
                key_ord.pop()
        elif len(plaintext_ord) > len(key_ord):
            add = len(plaintext_ord) - len(key_ord)
            for i in range(add):
                key_ord.append(key_ord[i])

    zipped_list = zip(plaintext_ord, key_ord)
    total = [ x + y for (x, y) in zipped_list ]

    cipher_ord = [ i%94 for i in total ]

    cipher_alpha = [ k for i in cipher_ord for k,v in ord_dict.items() if i == v ]
    print('Ciphertext:\n',*cipher_alpha, sep='')

def vigenere_decrypt():
        
    ciphertext = input('Your Ciphertext:\n>>')
    key = input('Your Key:\n>>')

    ciphertext_ord = [ v for letter in ciphertext for k,v in ord_dict.items() if letter == k ]
    key_ord = [ v for letter in key for k,v in ord_dict.items() if letter == k ]

    if len(ciphertext_ord) != len(key_ord):
        if len(ciphertext_ord) < len(key_ord):
            add = len(key_ord) - len(ciphertext_ord)
            for i in range(add):
                key_ord.pop()
        elif len(ciphertext_ord) > len(key_ord):
            add = len(ciphertext_ord) - len(key_ord)
            for i in range(add):
                key_ord.append(key_ord[i])

    zipped_list = zip(ciphertext_ord, key_ord)
    total = [ x - y for (x, y) in zipped_list ]

    plain_ord = [ i+94 if i <= 0 else i%94 for i in total ]

    plain_alpha = [ k for i in plain_ord for k,v in ord_dict.items() if i == v ]
    print('Plaintext:',*plain_alpha, sep='')

vigenere_encrypt()
vigenere_decrypt()