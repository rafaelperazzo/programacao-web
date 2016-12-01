# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

#COMECE AQUI
m=input('digite o numero m de termos da formula de pi:')
e=input('digite o epsilon para o calculo da razao aurea:')

print('%.15f'%(funcoes.calcula_pi(m)))
print('%.15f'%(funcoes.calcula_razao_aurea(m,e)))
