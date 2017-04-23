# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthias: '))
Fe=int(input('Número de empates do Flaminthias: '))
Fs=int(input('Saldo de gols do Flaminthias: '))
pc=(Cv*3)+(Ce*1)
pf=(Fv*3)+(Ce*1)
if pc>pf:
    print('C')
elif pc==pf:
    if Cs>Fs:
        print('C')
    elif Cs==Fs:
        print('=')
else:
    print('F')