# -*- coding: utf-8 -*-
import math


n=int(input('digite o n: '))
num=1
deno=n
S=0
i=0
while (num<=n) and (deno>=1):
    S=S+num/deno
    num=num+1
    deno=deno-i
i=i+1
print('%.5d' %S)
    
    