# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthias: '))
Fe=int(input('Número de empates do Flaminthias: '))
Fs=int(input('Saldo de gols do Flaminthias: '))
pc=Cv*3+Ce
pf=Fv*3+Fe
if pc>pf:
    print('C')
if pf>pc:
    print('F')
if pc==pf:
    if cs>cf:
        print('C')
    if cf>cs:
        print('F')
    else:
        print('=')