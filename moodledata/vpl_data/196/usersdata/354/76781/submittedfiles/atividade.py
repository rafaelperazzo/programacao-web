# -*- coding: utf-8 -*-
import math


n=int(input('digite o n: '))
num=1
deno=n
S=0
while (num<n) and (deno>=1):
    S=S+num/deno
    num=num+1
    deno=deno-1
print('%.5d' %S)
    
    