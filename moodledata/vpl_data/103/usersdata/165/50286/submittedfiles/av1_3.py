# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0


for i in range(1,a+1,1):
    cont=cont+1
    if a%i==0 and b%i==0:
        mdc=i
    
    
print(mdc)
print(cont)
