# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv = input('Digite o número de vitórias do Cormengo: ')
Ce = input('Digite o número de empates do Cormengo: ')
Cs = input('Digite o saldo de gols do Cormengo: ')
Fv = input('Digite o número de vitórias do Flaminthias: ')
Fe = input('Digite o número de empates do Flaminthias: ')
Fs = input('Digite o saldo de gols do Flaminthias: ')
if (Cv*3)+(Ce*1) > (Fv*3)+(Fe*1):
    print('C')
elif (Cv*3)+(Ce*1) < (Fv*3)+(Fe*1):
    print('F')
elif (Cv*3)+(Ce*1) == (Fv*3)+(Fe*1):
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')