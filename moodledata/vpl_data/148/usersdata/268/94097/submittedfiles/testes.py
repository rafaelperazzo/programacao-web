# -*- coding: utf-8 -*-
n=int(input('Digite o valor superior da combinação : '))
m=int(input('Digite o valor inferior da combinação : '))
numerador=1
denominador=1
def fatorial (n):
    fatorial=1
    while (n>0):
        fatorial=fatorial*n
        n=n-1
    return(fatorial)
print(fatorial(n))