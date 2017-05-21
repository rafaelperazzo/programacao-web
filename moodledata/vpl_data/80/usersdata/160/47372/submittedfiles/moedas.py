# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite os valores disponíveis das moedas:'))
b=int(input('Digite os valores disponíveis das moedas:'))
c=int(input('Digite a cédula:'))

cont=0
soma=0
while (c>0):
    qa=c//a
    c=c%a
    qb=c//b
    c=c%b
    cont=cont+1
    soma=qa+qb==c
    if (cont>0):
        print(qb)
        print(qa)
    if cont<c:
        print('N')