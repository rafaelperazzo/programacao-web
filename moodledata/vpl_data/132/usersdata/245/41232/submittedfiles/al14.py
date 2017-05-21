# -*- coding: utf-8 -*-
n=int(input('Digite o numero de Pessoas:'))
c=1
o=0
while c<=n:
    i=float(input('Digite a idade:'))
    o=o+i
    t=o%n
    print('%.2f'%t)