# -*- coding: utf-8 -*-
from __future__ import division
import funcoes

m=input('digite o numero m de termos da formula de pi :')
epsilon=input('digite o epsilon para o calculo da razao aurea:')


print('o valor aproximado da razao_aurea e:%.15f'%funcoes.calcula_razao_aurea(m,epsilon))