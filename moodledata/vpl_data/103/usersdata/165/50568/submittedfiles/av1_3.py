# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
resto=a%b

while resto!=0:
    x=b%resto
    temp=resto
    b=temp
    resto=x
    cont=cont+1
            

print(mdc)
print(cont)
