# -*- coding: utf-8 -*-
n=int(input('Digite o valor de n:'))
contador=n-1
fatorial=n
while contador>0:
    fatorial=fatorial*contador
    contador=contador-1
print('o fatorial de %d é %d'%(n,fatorial))