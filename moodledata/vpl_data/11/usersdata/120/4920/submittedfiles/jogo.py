# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
cv=input('insira o numero de vitorias do cormengo:')
ce=input('insira o numero de empates do cormengo:')
cs=input('insira o saldo de gols do cormengo:')
fv=input('insira o numero de vitorias do flaminthias:')
fe=input('insira o numero de empates do flaminthias:')
fs=input('insira o saldo de gols do flamninthias:')
#PROCESSAMENTO
pc=(cv*3)+ce
pf=(fv*3)+fe
#SAIDA
if pc>pf or cs>fs:
    print('c')
if pc<pf or cs<fs:
   print('f')
else:
    print('=')
    

