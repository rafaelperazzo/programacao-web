# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrada
cv=input('Digite o numero de vitorias de cormengo:')
ce=input('Digite o numero de empate de cormengo:')
cs=input('Digite o numero de saldo de gols:')
fv=input('Digite o numero de vitorias de flaminthias:')
fe=input('Digite o numero de empate de flaminthias:')
fs=input('Digite o numero de saldo de gols:')

#Processamento e Saída
pc=(cv*3+ce)
pf=(fv*3+fe)

if pc>pf or cs>fs or cv>fv:
    print ('c')
elif pc<pf or cs<fs or cv<fv:
    print ('f')
elif pc==pf and cs==fs and cv==fv:
    print ('=')