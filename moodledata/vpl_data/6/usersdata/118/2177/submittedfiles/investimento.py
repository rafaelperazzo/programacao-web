# -*- coding: utf-8 -*-
from __future__ import division

#1
valori = input('digite o valor do investimento inicial:')
taxa = input('digite o valor da taxa de crescimento percentual em forma decimal:')

#2
invest1 = valori + (valori*taxa)
invest2 = invest1 + (invest1*taxa)
invest3 = invest2 + (invest2*taxa)
invest4 = invest3 + (invest3*taxa)
invest5 = invest4 + (invest4*taxa)
invest6 = invest5 + (invest5*taxa)
invest7 = invest6 + (invest6*taxa)
invest8 = invest7 + (invest7*taxa)
invest9 = invest8 + (invest8*taxa)
invest10 = invest9 + (invest9*taxa)

#3
print('%.2f '  %invest1)
print('%.2f '  %invest2)
print('%.2f '  %invest3)
print('%.2f '  %invest4)
print('%.2f '  %invest5)
print('%.2f '  %invest6)
print('%.2f '  %invest7)
print('%.2f '  %invest8)
print('%.2f '  %invest9)
print('%.2f '  %invest10)