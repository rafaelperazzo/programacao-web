# -*- coding: utf-8 -*-
n=int(input('Digite o valor superior da combinação : '))
m=int(input('Digite o valor inferior da combinação : '))

def fatorial (n):
    fatorial=1
    while (n>0):
        fatorial=fatorial*n
        n=n-1
    return(fatorial)
sub= n - m
comb= (fatorial(n))/((fatorial(sub))*(fatorial(m))
