 # -*- coding: utf-8 -*-
from __future__ import division
import funcoes


m=int(input('quantidade m de termos:'))
ep= input('epsilon:')

print ('%.15f'%calcula_pi(m))
print ('%.15f'%calcula_razao_aurea(m,ep))