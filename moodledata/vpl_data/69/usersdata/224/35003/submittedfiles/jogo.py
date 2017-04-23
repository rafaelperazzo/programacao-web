# -*- coding: utf-8 -*-
import math
cv=int(input('Número de vitórias do Cormengo: '))
ce=int(input('Número de empates do Cormengo: '))
cs=int(input('Saldo de gols do Cormengo: '))
fv=int(input('Número de vitórias do Flaminthias: '))
fe=int(input('Número de empates do Flaminthias: '))
fs=int(input('Saldo de gols do Flaminthias: '))
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