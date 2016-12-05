# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=input('digite o número m de termos da formula de pi:')
e=input('digite o e para calculo da razao aurea:')
print funcoes.calcula_pi(m)
print('o valor da razao aurea: %.15f'%funcoes.calcula_razao_aurea(m,e))