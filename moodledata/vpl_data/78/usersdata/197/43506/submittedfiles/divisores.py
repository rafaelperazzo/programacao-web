# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
cont=0
multiplo=1
while cont<n:
    if multiplo%a==0 or multiplo%b==0:
        multiplo=a
        print('a')
        cont=cont+1
    multiplo=multiplo+1