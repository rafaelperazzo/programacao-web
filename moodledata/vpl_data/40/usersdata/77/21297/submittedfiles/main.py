# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COME
m=input('Digite o numero de termos m da formula de pi:')
e=input('Digite o valor de epsilon para o calculo da razao aurea:')

print('%.15f'%(funcoes.calcula_pi(m)))
print('%.15f'%(funcoes.calcula_razao_aurea(m,e)))
