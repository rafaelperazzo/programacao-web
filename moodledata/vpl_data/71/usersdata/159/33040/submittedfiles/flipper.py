# -*- coding: utf-8 -*-
import math

P=int(input('Posição de P 0 ou 1:'))
R=int(input('Posição de R 0 ou 1:'))

if P==0:
    print('C')
elif P==1 and R==0:
    print('B')
elif P==1 and R==1:
    print('A')