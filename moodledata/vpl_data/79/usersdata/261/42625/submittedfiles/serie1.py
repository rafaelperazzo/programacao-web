# -*- coding: utf-8 -*-
import math
def serie():
    n = int(input("Qual a quantidade de termos que você quer verificar? "))
    c = 1
    while 1:
        if c%2==1:
            res = (c)/(c**2)
        else:
            res = -(c)/(c**2)
        c = c+1
        s = s + res
        print ("%f.5") %s
        if c==n+1:
            break

serie()


