# -*- coding: utf-8 -*-
import math


n=int(input('digite o n: '))
if (n<0) :
    n= n*-1
num=1
deno=n
S=0
while (num<=n):
    S=S+(num/deno)
    num=num+1
    deno=deno-1
print('%.5f' %S)
    
    