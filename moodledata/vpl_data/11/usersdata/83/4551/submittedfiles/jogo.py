# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('Digite o numero de vitorias do Cormengo: ')
ce=input('Digite o numero de empates do Cormengo: ')
cs=input('Digite o saldo de gols do Cormengo: ')
fv=input('Digite o numero de vitórias do flaminthians: ')
fe=input('Digite o numero de empates do flaminthians: ')
fs=input('Digite o saldo de gols do flaminthians: ')

pontuacaoc=(3*cv)+(1*ce)
pontuacaof=(3*fv)+(1*fe)

if pontuacaoc>pontuacaof:
    print ('C')
elif pontuacaoc<pontuacaof:
    print ('F')
else:
    if cs>fs:
        print ('C')
    elif cs<fs:
        print ('F')
    else:
        print ('=')
        