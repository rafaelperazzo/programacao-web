# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o número de vitórias do Cormengo:')
Ce=input('Digite o número de empates do Cormengo:')
Cs=input('Digite o saldo de gols do Cormengo:')
Fv=input('Digite o número de vitórias do flaminthians:')
Fe=input('Digite o número de empates do flaminthians:')
Fs=input('Digite o saldo de gols do flaminthians:')

P1= (Cv*3)+(Ce*1)
P2= (Fv*3)+(Fe*1)

if P1>P2 :
    print('C')
elif P1<P2:
    print('F')
else:
    print('=')
