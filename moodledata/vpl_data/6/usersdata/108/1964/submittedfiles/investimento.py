# -*- coding: utf-8 -*-
from __future__ import division

inv = input ('Digite o valor do investimento inicial:')
per = input ('Digite a taxa de crescimento percentual:')

ano1 = inv+(inv*per)
ano2 = ano1+(ano1*per)
ano3 = ano2+(ano2*per)
ano4 = ano3+(ano3*per)
ano5 = ano4+(ano4*per)
ano6 = ano5+(ano5*per)
ano7 = ano6+(ano6*per)
ano8 = ano7+(ano7*per)
ano9 = ano8+(ano8*per)
ano10 = ano9+(ano9*per)

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
