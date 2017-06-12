# -*- coding: utf-8 -*-
soma1=0
cont1=0
soma2=0
cont2=0
i=0
n=int(input('digite o numero de elementos da lista:'))

for i in range(1,n+1,1):
    m=int(input('digite um valor:'))
    if m%2==1:
        soma1=soma1+m
        cont1=cont1+1
    else:
        soma2=soma2+m
        cont2=cont2+1
print(soma1)
print(soma2)
print(cont1)
print(cont2)
    
    
