# -*- coding: utf-8 -*-
import math
cv=int(input('Número de vitórias do Cormengo: '))
ce=int(input('Número de empates do Cormengo: '))
cs=int(input('Saldo de gols do Cormengo: '))
fv=int(input('Número de vitórias do Flaminthias: '))
fe=int(input('Número de empates do Flaminthias: '))
fs=int(input('Saldo de gols do Flaminthias: '))
a=cv*3
b=fv*3
if a>b:
    print('C')
    if b>a:
        print('F')
else
