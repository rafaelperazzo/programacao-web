# -*- coding: utf-8 -*-

n=int(input('Digite a : '))

def primo (x):
    i=2
    cont=0
    while(i<x):
        if ((x%i)==0):
            cont=cont+1
        i=i+1
    if cont==0:
        return(0)
    else:
        return(100)
        
        
print(primo(n))
while (n>0):
    parcela= n%10
    