# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI
investimento = float(input('Digite o seu investimento: '))
taxa = float(input('Digite a taxa de crescimento: '))

ano1 = investimento + (taxa*investimento)
ano2 = ano1 + (taxa*investimento)
ano3 = ano2 + (taxa*investimento)
ano4 = ano3 + (taxa*investimento)
ano5 = ano4 + (taxa*investimento)
ano6 = ano5 + (taxa*investimento)
ano7 = ano6 + (taxa*investimento)
ano8 = ano7 + (taxa*investimento)
ano9 = ano8 + (taxa*investimento)
ano10 = ano9 + (taxa*investimento)

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
