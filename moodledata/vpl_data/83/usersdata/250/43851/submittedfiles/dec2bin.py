# -*- coding: utf-8 -*-
n=int(input('digite um a valor:'))
i=0
soma=0
contador=0
while n//2==0:
    resto=n%2
    soma=soma+resto*(10**i)
    contador=contador+1
    i=i+1
print('%d'%soma)
    

