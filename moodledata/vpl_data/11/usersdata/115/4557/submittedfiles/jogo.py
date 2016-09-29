# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('digite o número de vitórias do cormengo:')
Ce=input('digite o número de empates do cormengo:')
Cs=input('digite o saldo de gols do cormengo:')
Fv=input('digite o número de vitórias do flaminthians:')
Fe=input('digite o número de empates do flaminthians:')
Fs=input('digite o saldo de gols do flaminthians:')

pontuacaoC=(3*Cv)+(1*Ce)
pontuacaoF=(3*Fv)+(1*Fe)

if pontuacaoC>pontuacaoF:
    print ('C')
elif pontuacao<pontuacaoF:
    print ('F')
else:
    if Cs>Fs:
        print ('C')
    elif Cs<Fs:
        print ('F')
    else:
        print ('=')
    