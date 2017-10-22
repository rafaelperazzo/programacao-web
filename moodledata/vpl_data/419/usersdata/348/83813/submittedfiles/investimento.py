# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

v1 = float(input( 'valor do investimento inicial: '))
tx = float(input( 'taxa de crescimento percentual: '))

while(true):
    v1 = v1 + v1*tx
    print ('%.2f' %v1)
    

