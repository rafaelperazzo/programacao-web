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
        
        #i = int(i)
        dec = dec + i*(2**exp)
        exp = exp-1
    print (int(dec))

bintodecimal()