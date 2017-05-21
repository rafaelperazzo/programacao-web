# -*- coding: utf-8 -*-
def bintodecimal():
    b = str(input("Qual binário você quer transformar? "))
    exp = len(b)-1
    dec = 0
    for i in b:
        if i == str(1):
            i = int(1)
        elif i == str(0):
            i = int(0)
        print (type(i))
        #i = int(i)
        dec = dec + i*(2**exp)
        print (type(i))
        exp = exp-1
    print (dec)
    print (type(dec))

bintodecimal()