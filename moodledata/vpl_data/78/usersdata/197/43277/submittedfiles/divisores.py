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
        Mb=Mb+1
        print(Ma)
    elif Mb<Ma:
        Mb%2==0
        Ma=Ma+1
        Mb=Mb+1
        print(Mb)
    else:
        Ma=Ma+1
        Mb=Mb+1
        print(Mb)
    cont=cont+1