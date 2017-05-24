# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
resto=1
cont=0
while resto>0:
    resto=a%b
    proximo=b%resto
    b=resto
    cont=cont+1
print(resto)
print(cont)