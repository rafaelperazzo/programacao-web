# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
inv=input('Digite o valor do investimento:')
t=input('Digite o valor da taxa anual:')

ano1=inv+t*inv
ano2=ano1+t*ano1
ano3=ano2+t*ano2
ano4=ano3+t*ano3
ano5=ano4+t*ano4
ano6=ano5+t*ano5
ano7=ano6+t*ano6
ano8=ano7+t*ano7
ano9=ano8+t*ano8
ano10=ano9+t*ano9

print('%.2f'%ano1)
print('%.2f'%ano2)
print('%.2f'%ano3)
print('%.2f'%ano4)
print('%.2f'%ano5)
print('%.2f'%ano6)
print('%.2f'%ano7)
print('%.2f'%ano8)
print('%.2f'%ano9)
print('%.2f'%ano10)