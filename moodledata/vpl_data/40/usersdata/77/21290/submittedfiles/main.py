# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COME
m=input('Digite a quantidade de termos m:')
e=input('Digite o valor de epsilon:')

print('%.15f'%(funcoes.calcula_pi(m)))
print('%.15f'%(funcoes.calcula_razao_aurea(m,e)))
