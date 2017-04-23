# -*- coding: utf-8 -*-
n=int(input('Quantidade de divisores a serem mostrados:'))
a=int(input('Número 1:'))
b=int(input('Número 2:'))  
múltiplo=1
for termo in range(1,n+1,1):
    if múltiplo%a==0 or múltiplo%b==0:
        múltiplo=múltiplo+1
        print(múltiplo)
    