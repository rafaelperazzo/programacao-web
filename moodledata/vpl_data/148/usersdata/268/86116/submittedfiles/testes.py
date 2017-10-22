# -*- coding: utf-8 -*-

n=int(input('Digite a : '))
soma = 0
cont2=0

def primo (x):
    i=2
    cont=0
    while(i<=x):
        if ((x%i)==0):
            cont=cont+1
        i=i+1
    if cont==0:
        return(10000)
    else:
        return(0)
        
        
while (n>0):
    parcela= n%10
    X9= primo(parcela)
    if X9==10000:
        print(parcela)
        cont2=cont2+1
    soma = soma + X9
    n=n//10
if soma>=20000:
    print('Sim')
if soma<20000:
    print('Nao')
    
    
    