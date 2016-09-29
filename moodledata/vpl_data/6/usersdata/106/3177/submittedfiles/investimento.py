# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
v = input ('Digite o valor do investimento inicial:')
i = input ('Digite o valor da taxa de crescimento percentual anual:')

#i = i/100
ano1 = v+v*i
ano2 = ano1 + ano1*i
ano3 = ano2 + ano2*i
ano4 = ano3 + ano3*i
ano5 = ano4 + ano4*i
ano6 = ano5 + ano5*i
ano7 = ano6 + ano6*i
ano8 = ano7 + ano7*i
ano9 = ano8 + ano8*i
ano10 = ano9 + ano9*i

print ('%.2f' %ano1)
print ('%.2f' %ano2)
print ('%.2f' %ano3)
print ('%.2f' %ano4)
print ('%.2f' %ano5)
print ('%.2f' %ano6)
print ('%.2f' %ano7)
print ('%.2f' %ano8)
print ('%.2f' %ano9)
print ('%.2f' %ano10)