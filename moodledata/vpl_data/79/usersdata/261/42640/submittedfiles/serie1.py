# -*- coding: utf-8 -*-
import math
def serie():
    n = int(input("Qual a quantidade de termos que você quer verificar? "))
    c = float(1)
    s = 1
    while 1:
        
        if c%2==1:
            res = (c)/(c**2)
        else:
            res = -(c)/(c**2)
        s = s + res
        print ("%.5f") % s
        c = c+1
        if c==n+1:
            break

serie()


