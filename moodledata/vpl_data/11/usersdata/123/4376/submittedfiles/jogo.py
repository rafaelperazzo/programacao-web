# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv= input('Insira a quantidade de vitórias do Cormengo:')
Ce= input('Insira a quantidade de empates do Cormengo:')
Cs= input('Insira o saldo de gols do Cormengo:')
Fv= input('Insira a quantidade de vitórias do Flaminthians:')
Fe= input('Insira a quantidade de empates do Flaminthians:')
Fs= input('Insira o slado de gols do Flaminthians:')

Cpv= Cv*3
Fpv= Fv*3

if (Cpv+Ce)>(Fpv+Fe):
    print('C')
elif (Cpv+Ce)<(Fpv+Fe):
    print('F')
elif (Cpv+Ce)==(Fpv+Fe):
    if Cs==Fs:
        print ('=')
    elif Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')