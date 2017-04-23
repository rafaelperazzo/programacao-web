# -*- coding: utf-8 -*-
import math
Cv=int(input('Informe as virtórias do Cormengo: '))
Ce=int(input('Informe os empates do Cormengo: '))
Cs=int(input('Informe o saldo de gols do Cormengo: '))
Fv=int(input('Informe as virtórias do Flaminthians: '))
Fe=int(input('Informe os empates do Flaminthians: '))
Fs=int(input('Informe o saldo de gols do Flaminthians: '))

Ctotal=(Cv*3)+Ce
Ftotal=(Fc*3)+Fe

if Cv>Fv:
    print('C')
elif Cv<Fv:
    print('F')
else:
    if Ctotal>Ftotal:
        print('C')
    elif Ctotal<Ftotal:
        print('F')
    else:
        if Cs>Fs:
            print('C')
        elif Cs<Fs:
            print('F')
        else:
            print('=')