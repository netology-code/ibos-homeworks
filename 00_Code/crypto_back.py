# -*- coding: utf-8 -*-

plain_text = "Очень секретная информация"
ciphertext = ""

i = len(plain_text) - 1

while i >= 0:
    ciphertext = ciphertext + plain_text[i]
    i = i - 1

print(ciphertext)

