# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
cont=0
resto=1
if a>b:
    while resto>0:
        resto=a%b
        cont=cont+1
        a=b
        b=resto
        if a%b==0:
            cont=cont+1
            break
    print(resto)
    print(cont)