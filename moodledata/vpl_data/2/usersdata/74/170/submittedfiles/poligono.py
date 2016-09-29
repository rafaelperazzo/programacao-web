# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o numero de lados dos poligono')

nd = n*((n-3)/2)

print('Um poligono com %d lados tem %d diagonais diferentes'% (n,nd))