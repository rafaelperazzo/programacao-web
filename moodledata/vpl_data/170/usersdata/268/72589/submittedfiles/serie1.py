# -*- coding: utf-8 -*-
import math

n=int(input('Digite n: '))
soma=0 
num=1
den=1

while(num<=n):
    if (num)%2!=0:
        soma=soma + num/den
        num= num+1
        den= num**2
    else:
        soma=soma - num/den
        num= num+1
        den= num**2
print(soma)