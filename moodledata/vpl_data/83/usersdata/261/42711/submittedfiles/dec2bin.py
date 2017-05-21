# -*- coding: utf-8 -*-
def dectobin():
    d = int(input("Qual o número você deseja transformar? "))
    bi = ""
    while d>0:
        bi = bi+str(d%2)
        print (bi[::-1])
        d = d//2
        print (d)

    
    
dectobin()