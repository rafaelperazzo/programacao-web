# -*- coding: utf-8 -*-
n=int(input('Quantidade de divisores a serem mostrados:'))
a=int(input('Número 1:'))
b=int(input('Número 2:'))  
multiplo=1
cont=0
while cont<n:
    if multiplo%a==0 or multiplo%b==0:
        cont=cont+1
        print(multiplo)
    multiplo=multiplo+1    