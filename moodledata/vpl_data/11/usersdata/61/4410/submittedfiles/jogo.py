# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Digite o número de vitórias de Cormengo: ')
Ce=input('Digite o número de empates de Cormengo: ')
Cs=input('Digite o número de saldo de gols do Cormengo: ')
Fv=input('Digite o número de vitórias de Flaminthians: ')
Fe=input('Digite o número de empates de Flaminthians: ')
Fs=input('Digite o número de saldo de gols do Flaminthians: ')
Pc=(Cv*3)+(Ce*1)
Pf=(Fv*3)+(Fe*1)
if Pc>Pf:
    print ('C')
elif Pc<Pf:
    print ('F')
else:
    if Cs>Fs:
        print ('C')
    if Cs<Fs:
        print ('F')
    