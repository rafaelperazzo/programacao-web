# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
i=1
numerador=1
a=0
s=0
if n<0:
    n=n*-1
else:
    n=n
    
while i<=n:
    s=(numerador)/(n+a)+s
    i=i+1
    a=a-1
    numerador=numerador+1
print(' %.5f ' %s)    
    

