# -*- coding: utf-8 -*-
import math
from decimal import *
getcontext().prec= 5
def serie():
    n = int(input("Qual a quantidade de termos que você quer verificar? "))
    c = 1
    s = 0
    while 1:
        
        if c%2==1:
            res = float((c)/(c**2))
        else:
            res = float(-(c)/(c**2))
        
        s = s + res
        
        c = c+1
        
        if c==n+1:
            break
    s = float(s)    
    print (s)

serie()


