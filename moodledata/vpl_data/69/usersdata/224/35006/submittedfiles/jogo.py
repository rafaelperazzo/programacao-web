# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthias: '))
Fe=int(input('Número de empates do Flaminthias: '))
Fs=int(input('Saldo de gols do Flaminthias: '))
pc=(cv*3)+(ce*1)
pf=(fv*3)+(ce*1)
if pc>pf:
    print('C')
elif pc==pf:
    if cs>fs:
        print('C')
elif cs==fs:
        print('=')
    else:
        print('F')
else:
    print('F')