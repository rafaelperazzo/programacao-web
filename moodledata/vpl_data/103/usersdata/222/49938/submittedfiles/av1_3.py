# -*- coding: utf-8 -*-
import math
a=int(input('a:'))
b=int(input('b:'))
resto=0
cont=0
while resto>0:
    a=a//b
    resto=a%b
    b=resto
    cont=cont+1
print(resto)
print(cont)