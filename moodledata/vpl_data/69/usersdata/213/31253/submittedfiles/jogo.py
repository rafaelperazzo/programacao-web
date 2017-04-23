# -*- coding: utf-8 -*-
import math

Fv=int(input('Informe as virtórias do Flaminthians: '))
Fe=int(input('Informe os empates do Flaminthians: '))
Fs=int(input('Informe o saldo de gols do Flaminthians: '))
Cv=int(input('Informe as virtórias do Cormengo: '))
Ce=int(input('Informe os empates do Cormengo: '))
Cs=int(input('Informe o saldo de gols do Cormengo: '))

Ftotal=(Fv*3)+Fe
Ctotal=(Cv*3)+Ce

if Fv>Cv:
    print('F')
elif Fv<Cv:
    print('C')
else:
    if Ftotal>Ctotal:
        print('F')
    elif Ftotal<Ctotal:
        print('C')
    else:
        if Fs>Cs:
            print('F')
        elif Fs<Cs:
            print('C')
        else:
            print('=')