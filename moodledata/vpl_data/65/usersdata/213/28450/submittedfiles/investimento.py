# -*- coding: utf-8 -*-
from __future__ import division

valorInvestido=float(input('Informe o valor do investimento inicial: '))
taxaDeCrescimento=float(input('Informe a taxa de crescimento percentual: '))

ano1=valorInvestido+(valorInvestido*taxaDeCrescimento) 
ano2=ano1+(ano1*taxaDeCrescimento)
ano3=ano2+(ano2*taxaDeCrescimento)
ano4=ano3+(ano3*taxaDeCrescimento)
ano5=ano4+(ano4*taxaDeCrescimento)
ano6=ano5+(ano5*taxaDeCrescimento)
ano7=ano6+(ano6*taxaDeCrescimento)
ano8=ano7+(ano7*taxaDeCrescimento)
ano9=ano8+(ano8*taxaDeCrescimento)
ano10=ano9+(ano9*taxaDeCrescimento)

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
