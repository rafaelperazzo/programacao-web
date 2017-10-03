# -*- coding: utf-8 -*-
import math
Cv = int(input('Número de vitórias do Cormengo: '))
Ce = int(input('Número de empates do Cormengo: '))
Cs = int(input('Saldo de gols do Cormengo: '))
Fv = int(input('Número de vitórias do Flaminthians: '))
Fe = int(input('Número de empates do Flaminthians: '))
Fs = int(input('Saldo de gols do Flaminthians: '))
CPontos = Cv*3+Ce
FPontos = Fv*3+Fe
if CPontos>FPontos:
    print('C')
if FPontos>CPontos:
    print('F')
if FPontos==CPontos:
    if Cs>Fs:
        print('C')
    if Cs<Fs:
        print('F')
    if Cs==Fs:
        print('=')
