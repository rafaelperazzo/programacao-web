# -*- coding: utf-8 -*-
n=int(input('digite n:'))
contador=n+1
fatoral=n
while contador>0:
    fatorial=fatorial*contador
    contador=contador-1
    print('o fatoral de n é%d'%fatorial)