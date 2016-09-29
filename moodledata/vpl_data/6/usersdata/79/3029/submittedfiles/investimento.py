
# -*- coding: utf-8 -*-
from __future__ import division, os

#COMECE SEU CODIGO AQUI


#Entrada

A = input('Digite seu saldo em 2016: ')

#Processamento

B = (A*0.045 + A)

C = (B*0.045 + B)

D = (C*0.045 + C)

E = (D*0.045 + D)

F = (E*0.045 + E)

G = (F*0.045 + F)

H = (G*0.045 + G)

I = (H*0.045 + H)

J = (I*0.045 + I)

K = (J*0.045 + J)

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

