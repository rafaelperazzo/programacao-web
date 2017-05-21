# -*- coding: utf-8 -*-
import math
n=int(input('Digite a quantidade de múltiplos a serem mostrados:'))
a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número'))
Ma=0
Mb=0
cont=0
while cont>n:
    if Ma<Mb:
        Ma%a==0
        Ma=Ma+1
        print(Ma)
    elif Mb<Ma:
        Mj%2==0
        Mj=Mj+1
        print(Mj)
    else:
        Ma=Ma+1
        Mb=Mb+1
        print(Mj)
    cont=cont+1