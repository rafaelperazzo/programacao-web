# -*- coding: utf-8 -*-
import math
n=int(input('Digite um número: '))
s=0
for i in range (1,n+1,1):
    if (n%2==1):
        s=s+(n/(n**2))
    else:
        s=s-(n/(n**2))
print('%f.5' %s)        
