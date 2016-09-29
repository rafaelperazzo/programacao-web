# -*- coding: utf-8 -*-
from __future__ import division

investimento = input('valor inicial do investimento:')
tx = input('taxa de crescimento percentual:')

INV = investimento + (tx*investimento)
INV2 = INV + (tx*INV)
INV3 = INV2 + (tx*INV2)
INV4 = INV3 + (tx*INV3)
INV5 = INV4 + (tx*INV4)
INV6 = INV5 + (tx*INV5)
INV7 = INV6 + (tx*INV6)
INV8 = INV7 + (tx*INV7)
INV9 = INV8 + (tx*INV8)
INV10 = INV9 + (tx*INV9)

print ('%f' %INV)
print ('%f' %INV2)
print ('%f' %INV3)
print ('%f' %INV4)
print ('%f' %INV5)
print ('%f' %INV6)
print ('%f' %INV7)
print ('%f' %INV8)
print ('%f' %INV9)
print ('%f' %INV10)


