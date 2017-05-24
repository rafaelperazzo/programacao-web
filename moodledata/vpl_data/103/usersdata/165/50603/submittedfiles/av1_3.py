# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0

for i in range(2,a+1,1):
    if a%i==0 and b%i==a:
        mdc=i
        cont=cont+1
        

print(mdc)
print(cont)

