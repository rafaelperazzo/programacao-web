# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthians: '))
Fe=int(input('Número de empates do Flaminthians: '))
Fs=int(input('Saldo de gols do Flaminthians: '))
if Cv>Fv:
    print('C')
    else:
        print('F')
if Ce==Fe:
    print('=')

