# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor a ser sacado:'))
vinte=(a-(a%20))/20
if vinte>0:
    a=a%20
dez=(a-(a%10))/10
if dez>0:
    a=a%10
cinco=(a-(a%5))/5
if cinco>0:
    a=a%5
dois=(a-(a%2))/2
if cinco>0:
    a=a%2    
um=a

print('Notas de vinte: %d' %vinte)
print('Notas de dez: %d' %dez)
print('Notas de cinco: %d' %cinco)
print('Notas de dois: %d' %dois)
print('Notas de um: %d' %um)