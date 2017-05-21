# -*- coding: utf-8 -*-
import math
n=int(input('digite n: '))
i=1
num=1
den=1
neg=-1
cont=0
soma=0
while cont<n:
    soma= soma + num/den
    num= num+1
    den= 2*num + den
    if soma%2==0:
        soma=soma*neg
    cont=cont+1
print(soma)