# -*- coding: utf-8 -*-
import math

Cv=int(input('Digite o numero de vitorias do Cormengo:'))
Ce=int(input('Digite o numero de empates do Cormengo:'))
Cs=int(input('Digite o numero de gols do Cormengo:'))
Fv=int(input('Digite o numero de de vitorias do Flaminthians:'))
Fe=int(input('Digite o numero de empates do Flaminthians:'))
Fs=int(input('Digite o numero de gols do Flaminthians:'))

if (Cv*3+Ce)>(Fv*3+Fe):
    print('C')
if (Cv*3+Ce)<(Fv*3+Fe):
    print('F')
if (Cv*3+Ce)==(Fv*3+Fe):
    if Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')
    elif Cs==Fs:
        print('=')
