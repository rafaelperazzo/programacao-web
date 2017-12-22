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

sub= n - m
comb1= (fatorial(n)) / ( (fatorial(sub))*(fatorial(m)) )
print(comb)

sub= a - b
comb2= (fatorial(a)) / ( (fatorial(sub))*(fatorial(b)) )
print(comb2)

sub= p - q
comb3= (fatorial(p)) / ( (fatorial(sub))*(fatorial(q)) )
print(comb3)

resultado= comb1*comb2/comb3
print(resultado)