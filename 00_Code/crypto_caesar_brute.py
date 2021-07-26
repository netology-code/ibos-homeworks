# -*- coding: utf-8 -*-

ciphertext = 'ЫпфъпьчкЙжтчюшъцкАтЙжшжъэыыфтяжякфпъкя'

aphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ\
    абвгдежзийклмнопрстуфхцчшщъыьэюя'
    
for key in range(len(aphabet)):
    plain_text = ''
    
    for symbol in ciphertext:
        if symbol in aphabet:
            num = aphabet.find(symbol)
            num = num - key
       
            if num < 0:
                num = num + len(aphabet)

            plain_text = plain_text + aphabet[num]
        else:
            plain_text = plain_text + symbol
        
    print(key, ":", plain_text)

