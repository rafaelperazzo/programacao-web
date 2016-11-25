# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite valor de m de termons:')
e=input('digite valor do epsilon:')

print('%.15f'%(funcoes.calcula_pi(m)))
print('%.15f'%(funcoes.calcula_razao_aurea(m,e)))