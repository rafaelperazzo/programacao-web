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
X=total de pontos de vitória do Carmengo
Y=total de pontos de empate do Carmengo
X2=total de pontos de vitória do Flaminthians
Y2=total de pontos de empate do Flaminthians
Cv*v==X
Ce*e==Y
Fv*v==X2
Fe*e==Y2
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