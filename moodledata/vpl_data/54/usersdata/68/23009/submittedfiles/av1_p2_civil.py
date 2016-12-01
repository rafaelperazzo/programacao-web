# -*- coding: utf-8 -*-
from __future__ import division

n=input ('Digite a quantidade de pinos:')
m=input ('Digite a aluta para a fechadura ser desbloqueada:')
alturas=[]
soma=0
i=0

for i in range (0,n,1):
    alturas.append (input('Digite a altura do pino:'))

while i<len(alturas):
    soma=soma+alturas[i]-alturas[i+1]
    i=i+1
    
if soma<0:
    soma=soma*(-1)

print soma