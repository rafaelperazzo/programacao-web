# -*- coding: utf-8 -*-
import math
cv=int(input('Digite o número de vitórias do Cormengo: '))
ce=int(input('Digite o número de empate do Cormengo: '))
cs=int(input('Digite o número de saldo de gols do Cormengo: '))
fv=int(input('Digite o número de vitórias do Flaminthians: '))
fe=int(input('Digite o número de empate do Flaminthians: '))
fs=int(input('Digite o número de saldo de gols do Flaminthians: '))
xc=(cv*3)+ce
xf=(fv*3)+fe
if xc>xf:
    print('C')
elif xc<xf:
    print('F')
else:
    if cs>fs:
        print('C')
    elif cs<fs:
        print('F')
    else:
        print('=')
        
    
            