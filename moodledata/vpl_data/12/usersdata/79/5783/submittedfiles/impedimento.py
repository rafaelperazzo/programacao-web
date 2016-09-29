# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI
R>50 e L<R e R>D

#Entrada

L = float(input('Digite a posiçao de "L", de 0 a 100: '))
R = float(input('Digite a posiçao de "R", de 0 a 100: '))
D = float(input('Digite a posiçao de "D", de 0 a 100: '))

#Processamento e Saída

if (R > 50) and (L < R) and (R > D):
    print('S')
    
else:
    print('N')
    

