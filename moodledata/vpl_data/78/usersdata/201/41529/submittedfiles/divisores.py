# -*- coding: utf-8 -*-
import math
n=int(input('Quantidade de multiplos a serem mostrados:'))
a=int(input('Primeiro numero:'))
b=int(input('Segundo numero:'))
multiplo=1
cont=0
while cont<n:
    if multiplo%a==0 or multiplo%b==0:
        cont=cont+1
        print(multiplo)
    multiplo=multiplo+1
