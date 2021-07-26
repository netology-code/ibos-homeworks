# -*- coding: utf-8 -*-

import os

path = "c:\windows"
#path = "c:\windows1"

if os.path.exists(path):
    print("Каталог", path, "сущестует")
else:
    print("Каталог", path, "не сущестует")