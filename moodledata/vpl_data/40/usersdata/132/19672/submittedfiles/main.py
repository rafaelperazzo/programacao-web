# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite o numero m termos da formula do pi:')
c=funcoes.pi(m)
print('%.15f'%c)
e=input('digite o valor de epsilon para o calculo da razao aurea:')
a=funcoes.aurea(m,e)
print('%.15f'%a)