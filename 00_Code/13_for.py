# -*- coding: utf-8 -*-

import os

last = 10
mask = "127.0.0."


for i in range(1, last):

    host = mask + str(i)
    result = os.system("ping -n 1 -w 1 " + host)

    if not result:
        print("Хост", host, "сущестует")
    else:
        print("Хост", host, "не сущестует")
