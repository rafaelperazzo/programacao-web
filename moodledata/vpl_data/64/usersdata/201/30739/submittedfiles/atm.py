# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
x=int(input('Valor do saque:'))
Vinte=(x-x%20)/20
if Vinte>0:
    x=x%20
Dez=(x-x%10)/10
if Dez>0:
    x=x%10
Cinco=(x-x%5)/5
if Cinco>0:
    x=x%5
Dois=(x-x%2)/2
if Dois>0:
    x=x%2
    
