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
    print(a)
    print(cont)
else:
    while resto>0:
        resto=b%a
        cont=cont+1
        b=a
        a=resto
    print(b)
    print(cont)