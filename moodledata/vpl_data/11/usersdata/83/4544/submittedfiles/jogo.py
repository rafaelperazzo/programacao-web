# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('Digite o numero de vitorias do Cormengo: ')
ce=input('Digite o numero de empates do Cormengo: ')
cs=input('Digite o saldo de gols do Cormengo: ')
fv=input('Digite o numero de vitórias do flaminthians: ')
fe=input('Digite o numero de empates do flaminthians: ')
fs=input('Digite o saldo de gols do flaminthians: ')

if cv>fv:
    print ('Cormengo está na frente')
elif cv<fv:
    print ('Flaminthians está na frente')
else :
    if ce>fe:
        print ('Cormengo está na frente')
    elif ce<fe:
        print ('Flaminthians está na frente')
    else :
        if cs>fs:
            print ('Cormengo está na frente')
        elif cs<fs:
            print ('Flaminthians está na frente')
        else :
            print ('Cormengo e Flaminthians estão empatados')
            