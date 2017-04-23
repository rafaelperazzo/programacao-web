# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de Vitórias do Cormengo: '))
Ce=int(input('Número de Empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de Vitórias do Flaminthians: '))
Fe=int(input('Número de Empates do Flaminthians: '))
Fs=int(input('Saldo de gols do Flaminthians: '))
if Cv>Fv:
    print('C')
elif Cv=Fv:
    if Ce>Fe:
        print('C')
    elif Ce=Fe:
        if Cs>Fs:
            print('C')
elif Cv=Fv and Ce=Fe and Cs=Fs:
    print('=')
else:
    print('F')