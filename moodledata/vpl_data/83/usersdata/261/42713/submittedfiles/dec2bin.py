# -*- coding: utf-8 -*-
def dectobin():
    d = int(input("Qual o número você deseja transformar? "))
    bi = ""
    while d>0:
        bi = bi+str(d%2)
        d = d//2
        #print (d)
    print (int(bi[::-1]))
    
    
dectobin()