
# -*- coding: utf-8 -*-
from __future__ import (division)

import os

#COMECE SEU CODIGO AQUI


#Entrada

A = input('Digite seu saldo em 2016: ')
x = input('Digite a taxa: ')

#Processamento

B = (A*x + A)

C = (B*x + B)

D = (C*x + C)

E = (D*x + D)

F = (E*x + E)

G = (F*x + F)

H = (G*x + G)

I = (H*x + H)

J = (I*x + I)

K = (J*x + J)

os.system("cls" if os.name == "nt" else 'clear')
#Saida

print('%.2f' %(B))

print('%.2f' %(C))

print('%.2f' %(D))

print('%.2f' %(E))

print('%.2f' %(F))

print('%.2f' %(G))

print('%.2f' %(H))

print('%.2f' %(I))

print('%.2f' %(J))

print('%.2f' %(K))

