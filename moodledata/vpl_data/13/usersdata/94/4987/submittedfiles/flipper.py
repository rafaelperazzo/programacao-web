# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

P=input('digite o valor de P,se ele e 0 ou 1:')
R=input('digite o valor de R,se ele e 0 ou 1:')

if P==0:
    print('C')
    
elif P==1 and R==0:
    print('B')

elif P==1 and R==1:
    print('A')