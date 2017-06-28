# -*- coding: utf-8 -*-
import math
def somatermos(a):
    soma=0
    while(n>1):
        soma=soma+a[i]**2
        if soma!=1:
            soma=soma+a[i]
        if soma==1:
            return True

n=int(input('Digite valor: '))
a=[]
for i in range(0,n,1):
    a.append(n)

if somatermos(a):
    print('Feliz')
else:
    print('Nao Feliz')