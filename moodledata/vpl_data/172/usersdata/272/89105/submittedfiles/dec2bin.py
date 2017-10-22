# -*- coding: utf-8 -*-

n=int(input('Digite n: '))
numero=n
soma=0
cont=0
while (n>0):
    numero=n
    numero=numero%2
    n=n//2
    soma=soma+(numero*(10**(cont)))
    cont=cont+1
print(soma)
    
    
    
