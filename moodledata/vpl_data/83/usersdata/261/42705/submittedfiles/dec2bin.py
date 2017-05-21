# -*- coding: utf-8 -*-
def dectobin():
    d = int(input("Qual o número você deseja transformar? "))
    bi = ""
    while d>0:
        bi = bi+d%2
        print (bi)
        d = d//2
        print (d)
        