# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o número de vitórias do Cormengo:')
Ce=input('Digite o número de empates do Cormego:')
Cs=input('Digite o saldo de gols do Cormengo:') 
Fv=input('Digite o número de vitórias do Flaminthians:')
Fe=input('Digite o número de empates do Flaminthians:')
Fs=input('Digite o saldo de gols do Flaminthians:')

Cs=((Cv*3)+Ce)
Fs=((Fv*3)+Fe)

if (Cs>Fs):
    print('C')
    
elif (Cs<Fs):
    print('F')
    
else:
    print('=')