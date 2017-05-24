# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
resto=1
cont=0
while resto>0:
    resto=a%b
    a=b
    b=resto
    cont=cont+1
    resto=resto+1
print(resto)
print(cont)