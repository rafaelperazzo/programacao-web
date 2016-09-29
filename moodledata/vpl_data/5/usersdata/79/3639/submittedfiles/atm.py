# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

#Entrada

v = int(input('Digite a quantidade a ser sacada: '))
D20 = 0
D10 = 0
D5 = 0
D2 = 0
D1 = 0

#Processamento

while v >= 20:
    D20 = D20 +1
    
    v = v - 20
    
while v= 10 < 20:
    D10 = D10 + 1
    
    v = v - 10
    
while v >= 5 < 10:
    D5 = D5 + 1
    
    v = v - 5
while v >= 2 < 5:
    D2 = D2 + 1
    
    v = v - 2

while v >= 1 < 2:
    D1 = D1 + 1
    
    v = v - 1
    
#Saida

print ('Numero de cedulas de 20: ') +str(D20)
print ('Numero de cedulas de 10: ') +str(D10)
print ('Numero de cedulas de 5: ') +str(D5)
print ('Numero de cedulas de 2: ') +str(D2)
print ('Numero de cedulas de 1: ') +str(D1)

    