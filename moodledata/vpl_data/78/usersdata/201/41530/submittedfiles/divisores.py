# -*- coding: utf-8 -*-
import math
n=int(input('Quantidade de multiplos a serem mostrados:'))
a=int(input('Primeiro numero:'))
b=int(input('Segundo numero:'))
multi=1
cont=0
while cont<n:
    if multi%a==0 or multi%b==0:
        cont=cont+1
        print(multi)
    multi=multi+1
