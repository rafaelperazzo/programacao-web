# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitorias do Cormengo:'))
Ce=int(input('digite o número de empates do Cormengo:'))
Cs=int(input('digite o saldo de gols do Cormengo:'))
Fv=int(input('digite o número de vitorias do Flaminthians:'))
Fe=int(input('digite o número de vitorias do Flaminthians:'))
Fs=int(input('digite o saldo de gols do Flaminthans:'))
x=(Cv*3+Ce)
y=(Fv*3+Fe)
if x>y:
    print('C')
elif x<y:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')
    else:
        print('=')