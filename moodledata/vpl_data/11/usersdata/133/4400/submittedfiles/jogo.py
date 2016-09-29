# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Digite o número de vitórias do Cormengo:')
Ce=input('Digite o número de empates do Cormengo:')
Cs=input('Digite o saldo de gols do cormengo:')
Fv=input('Digite o número de vitórias do Flaminthians:')
Fe=input('Digite o número de empates do Flaminthians:')
Fs=input('Digite o saldo de gols do Flaminthians:')
a=3*Cv+Ce
b=3*Fv+Fe
if(a>b):
    print('C')
elif(a<b):
    print('F')
else:
    if (Cs>Fs):
        print('C')
    elif (Cs<Fs):
        print('F')
    else:
        print('=')
        