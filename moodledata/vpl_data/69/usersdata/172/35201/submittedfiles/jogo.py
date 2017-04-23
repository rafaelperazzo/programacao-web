# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitórias de c:'))
Ce=int(input('digite o número de empates de c:'))
Cs=int(input('digite o saldo de gols de c:'))
Fv=int(input('digite o número de vitórias de f:'))
Fe=int(input('digite o número de empates de f:'))
Fs=int(input('digite o saldo de gols de f:'))
a=Cv*3
b=Fv*3
e=a+Ce
f=b+Fe
if  e!=f:
    if  e>f:
        print('C')
    if  e<f:
        print('F')
elif    e==f:
    if  Cs>Fs:
        print('C')
    elif  Cs<Fs:
        print('F')
    else:
        print('=')
        
    