# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
#entrada
P=input('digite o valor de P:')
R=input('digite o valor de R:')
#processamento e saida 
if R==P  and R==1:
    print('A')
if R<P and R==0:
    print('B')
if P==0 and R==0:
    print('C')