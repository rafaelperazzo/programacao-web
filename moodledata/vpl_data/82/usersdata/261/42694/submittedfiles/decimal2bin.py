# -*- coding: utf-8 -*-
def bintodecimal():
    b = str(input("Qual binário você quer transformar? "))
    exp = len(b)-1
    dec = 0
    for i in b:
        i = int(i)
        dec = dec + i*(2**exp)
        exp = exp-1
    print (int(dec))

bintodecimal()