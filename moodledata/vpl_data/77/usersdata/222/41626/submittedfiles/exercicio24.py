# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
def mdc(a,b):
    resto=none
    while resto is not 0:
        resto=a%b
        a=b
        b=resto
    print(a)


    
