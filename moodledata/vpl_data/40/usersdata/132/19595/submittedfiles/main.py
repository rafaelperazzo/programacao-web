# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite o valor de m:')
c=funcoes.pi(m)
print('%.15f'%c)
e=input('digite o valor de epsilon:')
a=funcoes.aurea(c/5,e)
print(a)
