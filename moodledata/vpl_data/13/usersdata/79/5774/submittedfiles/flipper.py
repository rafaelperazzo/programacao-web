# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

#Entrada 

P = float(input('Digite "0" para a esquerda ou "1" para a direita: '))
R = float(input('Digite "0" para a esquerda ou "1" para a direita: '))

#Processamento e Saída

if P == 0:
    print('C')
    
if (P == 1) and (R == 1):
    print('A')
    
if (P == 1) and (R == 0):
    print('B')
    
    
    