# -*- coding: utf-8 -*-
for i in range(1000,9999,1):
    raiz=i**0.5
    d=i//100
    w=d+(i-d*100)
    if raiz==w:
        print(i)
        