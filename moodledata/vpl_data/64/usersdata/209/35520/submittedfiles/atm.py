# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
A=int(input('Saque:':))
VINTE=(A-A%20)/20
if VINTE>0:
    A=A%20
DEZ=(A-A%10)/10
if DEZ>0:
    A=A%10
CINCO=(A-A%5)/5
if CINCO>0:
    A=A%5
DOIS=(A-A%2)/2
if DOIS>0:
    A=A%2
UM=A
print('%.f'%VINTE)
print('%.f'%DEZ)
print('%.f'%CINCO)
print('%.f'%DOIS)
print('%.f'%UM)