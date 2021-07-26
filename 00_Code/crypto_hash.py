# -*- coding: utf-8 -*-

import hashlib

'''
text = "Секретная информация о русских хакерах".split()

for i in text:
    md5 = hashlib.md5(i.encode())
    print(i,":", md5.hexdigest())
'''

"""
print("Посимвольно:")
md5 = hashlib.md5()
md5.update(b"t")
print(md5.hexdigest())
md5.update(b"e")
print(md5.hexdigest())
md5.update(b"x")
print(md5.hexdigest())
md5.update(b"t")
print(md5.hexdigest())

md5 = hashlib.md5(b"text")
print("text:\n" + md5.hexdigest())
"""

'''
md5 = hashlib.md5(b"text")
print("MD5:", md5.hexdigest())
md5 = hashlib.sha1(b"text")
print("SHA-1:", md5.hexdigest())
md5 = hashlib.sha256(b"text")
print("SHA-256:", md5.hexdigest())
md5 = hashlib.sha512(b"text")
print("SHA-512:", md5.hexdigest())
'''

'''
text = "text"
salt = "salt"

md5 = hashlib.sha512(b"text")
print("SHA-512:", md5.hexdigest())

md5 = hashlib.sha512(salt.encode() + text.encode())
print("SHA-512 with salt:", md5.hexdigest())
'''

'''
import bcrypt

user_pass = "12345"
hashed_pass = bcrypt.hashpw(user_pass.encode(), bcrypt.gensalt())
print(hashed_pass)

user_text = input("Введите пароль:")

if bcrypt.hashpw(user_text.encode(), hashed_pass) == hashed_pass:
    print("Пароли совпадают.")
else:
    print("Пароли не совпадают.")
'''


'''
from Crypto.Cipher import AES
import os

key = os.urandom(16)
print("key: ", key.hex())
aes = AES.new(key, AES.MODE_EAX)

ciphertext, tag = aes.encrypt_and_digest(b"data")

print("Ciphertext:", ciphertext.hex())
'''


from Crypto.Cipher import AES
from Crypto import Random

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

plain_text = "Top secret1"
key = hashlib.sha256(b"12345").digest()
print("Key:", key)

plain_text = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = (iv + cipher.encrypt(plain_text.encode()))
print("\nCiphered text:", cipher_text)

cipher_text = cipher_text
iv = cipher_text[:BS]
cipher = AES.new(key, AES.MODE_CBC, iv )
plain_text = unpad(cipher.decrypt(cipher_text[BS:]))
print("\nPlain text:", plain_text)


