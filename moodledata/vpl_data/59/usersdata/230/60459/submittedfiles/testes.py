# -*- coding: utf-8 -*-
import math
def feliz(a):
    soma=0
    while(n>1):
        soma=soma+a[i]**2
        if soma!=1:
            soma=soma+a[i]
        if soma==1:
            return True

n=int(input('Digite valor: '))
a=feliz(n)
if feliz(a):
    print('Feliz')
else:
    print('Nao Feliz')