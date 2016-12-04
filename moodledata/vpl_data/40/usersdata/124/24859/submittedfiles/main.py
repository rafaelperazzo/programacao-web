# -*- coding: utf-8 -*-
from __future__ import division
import funcoes
import vabsol(m)

#COMECE AQUI
m = int(input('Digite o número m de termos da fórmula de pi:  '))
epsilon = input('Digite o epsilon para o cálculo da razão áurea: ')

m = vabsol(m)
print('Valor aproximado de pi: %.15f' %calculopi(m))
print('Valor aproximado da razão áurea: %.15f' %razaurea(m, epsilon))