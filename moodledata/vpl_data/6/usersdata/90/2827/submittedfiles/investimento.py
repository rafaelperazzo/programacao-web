# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
#Entrada
x=input('Digite aqui o valor do investimento inicial:')
y=input('Digite aqui a taxa de crescimento:')

#Processamento
ano1=(x*y)+x
ano2=(ano1*y)+ano1
ano3=(ano2*y)+ano2
ano4=(ano3*y)+ano3
ano5=(ano4*y)+ano4
ano6=(ano5*y)+ano5
ano7=(ano6*y)+ano6
ano8=(ano7*y)+ano7
ano9=(ano8*y)+ano8
ano10=(ano9*y)+ano9

#Saida
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