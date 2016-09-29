# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

P = input(' digite a direção da portinha P (0 para esquerda e 1 para direita): ')
R = input(' digite a direção da portinha R (0 para esquerda e 1 para direita): ')

if P == 1 and R == 1:
    print ('A')
if P == 0 and R == 0:
    print ('C')
if P == 1 and R == 0:
    print ('B')
if P == 0 and R == 1:
    print ('C')