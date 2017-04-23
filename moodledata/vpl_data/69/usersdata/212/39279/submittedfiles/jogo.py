# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitórias do cormengo:'))
Ce=int(input('digite o número de empates do cormengo:'))
Cs=int(input('digite o saldo de gols do cormengo:'))
Fv=int(input('digite o número de vitórias do flaminthians:'))
Fe=int(input('digite o número de empates do flamintihans:'))
Fs=int(input('digite o saldo de gols do flaminthians:'))
pontosc=(Cv*3)+(Ce)
pontosf=(FV*3)+(Fe)
if pontosc>pontosf:
    print('C')
elif pontosc<pontosf:
    print('F')
else:
    if  Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')
    else:
        print('=')