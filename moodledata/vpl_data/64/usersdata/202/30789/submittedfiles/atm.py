# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
a=int(input('valor do saque:'))
vinte=(x-x%20)/20
if vinte>0:
    x=x%20
dez=(x-x%10)/10
if dez>0:
    x=x%10
cinco=(x-x%5)/5
if cinco>0:
    x=x%5
dois=(x-x%2)/2
if dois>0:
    x=x%2
um=(x-x%1)/1
if um>0:
    x=0
    print('%d'%vinte)
    print('%d'%dez)
    print('%d'%cinco)
    print('%d'%dois)
    print('%d'%um)
    
