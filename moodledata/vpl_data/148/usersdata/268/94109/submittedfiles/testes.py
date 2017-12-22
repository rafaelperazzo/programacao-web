# -*- coding: utf-8 -*-
#Calculadora de Combinações

n=int(input('Digite o valor superior da combinação : '))
m=int(input('Digite o valor inferior da combinação : '))

a=int(input('Digite o valor superior da combinação : '))
b=int(input('Digite o valor inferior da combinação : '))

p=int(input('Digite o valor superior da combinação : '))
q=int(input('Digite o valor inferior da combinação : '))

def fatorial (n):
    fatorial=1
    while (n>0):
        fatorial=fatorial*n
        n=n-1
    return(fatorial)
    
def comb (n,m):
    sub= n - m
    comb= (fatorial(n)) / ( (fatorial(sub))*(fatorial(m)) )

numerador= comb(n,m)*comb(a,b)
denominador= comb(p,q)

print(numerador/denominador)




