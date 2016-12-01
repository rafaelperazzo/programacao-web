# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI


m=input('digite o numero m de termos da formula de pi:')
e=input('digite o epsilon para o calculo da razao aurea:')

print('%.15f'%(calcula_pi(m)))
print('%.15f'%(calcula_razao_aurea(m,e)))
