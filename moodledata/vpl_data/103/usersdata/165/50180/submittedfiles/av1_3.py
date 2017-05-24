# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
resto=a%b
while resto>0:
    mdc=b%resto
    b=resto
    resto=mdc
    cont=cont+1
    
print(mdc)
print(cont)
