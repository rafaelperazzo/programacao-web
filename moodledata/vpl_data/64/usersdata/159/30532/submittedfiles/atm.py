# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor a ser sacado:'))
vinte=(a-(a%20))/20
if vinte>0:
    b=a%20
dez=(b-(b%10))/10
if dez>0:
    c=b%10
cinco=(c-(c%5))/5
if cinco>0:
    d=c%5
dois=(d-(d%2))/2
if cinco>0:
    e=d%2    
um=e

print('Notas de vinte: %d' %vinte)
print('Notas de dez: %d' %dez)
print('Notas de cinco: %d' %cinco)
print('Notas de dois: %d' %dois)
print('Notas de um: %d' %um)