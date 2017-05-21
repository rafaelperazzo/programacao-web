# -*- coding: utf-8 -*-
import math
n=int(input('digite n:'))
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
for i in range(1,n+1,1):
    if a%i==0 or b%i==0:
        cont=cont+1
print(cont)
