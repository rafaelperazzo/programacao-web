# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero de lados do poligono')

a = (n-3)/2
nd = n*a

print('Um poligono com %d lados tem %d diagonais diferentes'% (n,nd))