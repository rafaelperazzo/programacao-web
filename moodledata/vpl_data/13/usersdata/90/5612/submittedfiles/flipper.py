# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI

#Entrada
P=input('Digite aqui o valor de P:')
R=input('Digite aqui o valor de R:')

#Processamento e Saida
if P==1 and R==1:
    print ('A')
else:
    if P==1 and R==0:
        print ('B')
else:
    if P==0:
        print ('C')