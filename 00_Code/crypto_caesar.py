# -*- coding: utf-8 -*-

plain_text = 'Секретная информация о русских хакерах'
key = 10

aphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ\
    абвгдежзийклмнопрстуфхцчшщъыьэюя'
ciphertext = ''

for symbol in plain_text:
    if symbol in aphabet:
        num = aphabet.find(symbol)
        num = num + key
       
        if num >= len(aphabet):
            num = num - len(aphabet)

        ciphertext = ciphertext + aphabet[num]

    else:
        ciphertext = ciphertext + symbol

print(ciphertext)

plain_text = ciphertext
ciphertext = ''

for symbol in plain_text:
    if symbol in aphabet:
        num = aphabet.find(symbol)
        num = num - key
        
        if num < 0:
            num = num + len(aphabet)

        ciphertext = ciphertext + aphabet[num]

    else:
        ciphertext = ciphertext + symbol

print(ciphertext)
