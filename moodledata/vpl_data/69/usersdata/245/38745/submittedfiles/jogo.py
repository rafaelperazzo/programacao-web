# -*- coding: utf-8 -*-
import math
cv=int(input('Digite o numero de vitorias:'))
ce=int(input('Digite o numero de empates:'))
cs=int(input('Digite o saldo de gols:'))
fv=int(input('Digite o numero de vitorias:'))
fe=int(input('Digite o numero de empates:'))
fs=int(input('Digite o saldo de gols:'))
c=cv*3
f=fv*3
if c>f:
    print('C')
elif c<f:
    print('F')
else:
    if ce>fe:
        print('C')
    elif ce<fe:
        print('F')
    else:
        if cs>fs:
            print('C')
        elif cs<fs:
            print('F')