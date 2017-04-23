# -*- coding: utf-8 -*-
import math
cv=int(input('Digite o número de vitórias do Cormengo: '))
ce=int(input('Digite o número de empate do Cormengo: '))
cs=int(input('Digite o número de saldo de gols do Cormengo: '))
fv=int(input('Digite o número de vitórias do Flaminthians: '))
fe=int(input('Digite o número de empate do Flaminthians: '))
fs=int(input('Digite o número de saldo de gols do Flaminthians: '))
if (cv>fv):
    print('C')
    elif (cv<fv):
        print('F')
        else:
            print('=')
if (ce>fe):
    print('C')
    elif (ce<fe):
        print('F')
        else:
            print('=')
if (cs>fs):
    print('C')
    elif (cs<fs):
        print('F')
        else:
            print('=')
    
            