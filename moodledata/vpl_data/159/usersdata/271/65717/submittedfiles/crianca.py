# -*- coding: utf-8 -*-
#ENTRADA
p1 = float(input(digite o valor do peso1: '))
c1 = float(input(digite o valor do comprimento1: '))
p2 = float(input(digite o valor do peso2: '))
c2 = float(input(digite o valor do comprimento2: '))
#PROCESSAMENTO
if (p1*c1)==(p2*c2) :
    print('0')
if (p1*c1)>(p2*c2) :
    print('-1')
if (p1*c1)<(p2*c2) :
    print('1')

