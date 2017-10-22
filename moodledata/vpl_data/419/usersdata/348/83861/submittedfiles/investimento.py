# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

v1 = float(input( 'valor do investimento inicial: '))
tx = float(input( 'taxa de crescimento percentual: '))
n = 10
v2 = (v1*(( 1 + tx)**n))

while v1 <= v2:
    v1 = v1 + v1*tx
    print ('%.2f' %v1)
    

