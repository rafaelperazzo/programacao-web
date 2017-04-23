# -*- coding: utf-8 -*-
import math
cv=int(input('Número de vitórias do Cormengo: '))
ce=int(input('Número de empates do Cormengo: '))
cs=int(input('Saldo de gols do Cormengo: '))
fv=int(input('Número de vitórias do Flaminthias: '))
fe=int(input('Número de empates do Flaminthias: '))
fs=int(input('Saldo de gols do Flaminthias: '))
a=(cv*3)+(ce*1)
b=(fv*3)+(ce*1)
if a>b:
    print('C')
elif a==b:
    if cs>fs:
        print('C')
    elif cs==fs:
        print('=')
    else:
        print('F')