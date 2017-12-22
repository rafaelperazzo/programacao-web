# -*- coding: utf-8 -*-
a = 80000
b = 200000
cont = 0

while a<=b:
    a = a*1.03
    b = b*1.015
    cont += 1

print(int(cont))

    