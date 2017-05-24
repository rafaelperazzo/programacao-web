# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
resto=a%b

while resto!=0:
    mdc=b%resto
    cont=cont+1
    b=resto
    resto=mdc
    
print(mdc)
print(cont)

