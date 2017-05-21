# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
n=6
multiplo=1
for i in range(1,n+1,1):
    if i%a==0 or i%b==0:
        multiplo=i
print(multiplo)        