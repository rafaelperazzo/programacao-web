# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada

cv= input ('Digite o número de vitórias do Cormengo:')
ce= input ('Digite o número de empates do Cormengo:')
cs= input ('Digite o saldo de gols do Cormengo:')
fv= input ('Digite o número de vitórias do Flamithians:')
fe= input ('Digite o número de empates do Flamithians:')
fs= input ('Digite o saldo de gols do Flamithians:')

#Processamento e Saida:

vc=((cv*3)+ce+cs)
vf=((fv*3)+fe+fs)

if (vc>vf):
    print ('C')
elif (vc<vf):
    print ('F')
else:
    print ('=') 
