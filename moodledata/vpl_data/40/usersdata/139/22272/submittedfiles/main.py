# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite o valor de m de termons:')
e=input('digite o valor de e de epsilon:')
print('%.15f'%(funcoes.calcula_pi(m)))
#print funcoes,calcula_cos
print('%.15f'%(funcoes.calcula_razao_aurea(m,e)))

