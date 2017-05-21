# -*- coding: utf-8 -*-
n=int(input('Quantidade de divisores a serem mostrados:'))
a=int(input('Número 1:'))
b=int(input('Número 2:'))  
multiplo=0
for i in range(1,n+1,1):
    if a%multiplo==0 or b%multiplo==0:
        multiplo=multiplo+1
        print(multiplo)