# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
cv=input('Digite o número de vitórias do Cormengo:')
ce=input('Digite o número de empates do Cormengo:')
cs=input('Digite o saldo de gols do Cormengo:')
fv=input('Digite o número de vitórias do Flaminthians:')
fe=input('Digite o número de empates do Flaminthians:')
fs=input('Digite o saldo de gols do Flaminthians:')
#PROCESSAMENTO
pc=(cv*3)+(ce*1)
pf=(fv*3)+(fe*1)
#SAÍDA
if pc>pf:
    print('C')
elif pc<pf:
    print('F')
else:
    if cs==fs:
        print('=')
    elif cs>fs:
        print('C')
    else:
        print('F')