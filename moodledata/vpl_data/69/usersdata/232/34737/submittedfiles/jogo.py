# -*- coding: utf-8 -*-
import math
Cv=int(input('Insira o número de vitórias do Cormengo: '))
Ce=int(input('Insira o número de empates do Cormengo: '))
Cs=int(input('Insira o saldo de gols do Cormengo: '))
Fv=int(input('Insira o número de vitórias do Flaminthians: '))
Fe=int(input('Insira o número de empates do Flaminthians: '))
Fs=int(input('Insira o saldo de gols do Flaminthians: '))
PontosC=((Cv*3)+(Ce*1))
PontosF=((Fv*3)+(Fe*1))
if PontosC>PontosF:
    print('C')
    if PontosC==PontosF and Cs>Fs:
        print('C')
        if PontosC==PontosF and Cs==Fs:
            print('=')
if PontosC<PontosF:
    print('F')
    if PontosC==PontosF and Cs<Fs:
        print('F')
        if PontosC==PontosF and Cs==Fs:
            print('=')
