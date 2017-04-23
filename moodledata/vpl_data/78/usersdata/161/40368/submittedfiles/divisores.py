# -*- coding: utf-8 -*-
n=int(input('Quantidade de divisores a serem mostrados:'))
a=int(input('Número 1:'))
b=int(input('Número 2:'))  
múlt=0
cont=0
while cont<n:
    if múlt%a==0 or múlt%b==0:
        múlt=múlt+1
        cont=cont+1
        print(múlt)
    