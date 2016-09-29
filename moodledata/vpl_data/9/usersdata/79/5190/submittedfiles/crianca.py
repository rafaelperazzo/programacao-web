# -*- coding: utf-8 -*-
from __future__ import division
 
#Entrada

P1 = float(input('Digite o peso da criança do lado esquerdo: '))
C1 = float(input('Digite o comprimento do lado esquerdo: '))
P2 = float(input('Digite o peso da criança do lado direito: '))
C2 = float(input('Digite o comprimento do lado direito: '))

#Processamento e Saída

if P1*C1 == P2*C2:
    print('0')
    
if P1*C1 > P2*C2:
    print('-1')
    
if P1*C1 < P2*C2:
    print('1')
    
