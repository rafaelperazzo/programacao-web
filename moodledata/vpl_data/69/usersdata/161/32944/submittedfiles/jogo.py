# -*- coding: utf-8 -*-
import math
Cv=int(input('Informe o número de vitórias do Carmengo:'))
Ce=int(input('Informe o número de empates do Carmengo:'))
Cs=int(input('Informe o saldo de gols do Carmengo:'))
Fv=int(input('Informe o número de vitórias do Flaminthians:'))
Fe=int(input('Informe o número de empates do Flaminthians:'))
Fs=int(input('Informe o saldo de gols do Flaminthians:'))
v=3
e=1
X=0
Y=0
X2=0
Y2=0
X=Cv*v
Y=Ce*e
X2=Fv*v
Y2=Fe*e
if X+Y>X2+Y2:
    print('C')
elif X2+Y2>X+X:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
    else:
        ('=')