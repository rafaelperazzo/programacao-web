# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
i=1
while i<=a:
    if a%i==0 and b%i==0:
        mdc=i
        cont=cont+1
        i=i+1    

print(mdc)
print(cont)
