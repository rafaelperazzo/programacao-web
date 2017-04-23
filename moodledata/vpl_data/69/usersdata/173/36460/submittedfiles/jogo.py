# -*- coding: utf-8 -*-
import math
cv=float(input('Digite o número de vitórias do Cormengo: '))
ce=float(input('Digite o número de empates do Cormengo: '))
cs=float(input('Digite o saldo de gols do Cormengo: '))
fv=float(input('Digite o número de vitórias do Flaminthians: '))
fe=float(input('Digite o número de empates do Flaminthians: '))
fs=float(input('Digite o saldo de gols do Flaminthians: '))
if((cv*3)+ce)>((fv*3)+fe):
    print('C')
elif((cv*3)+ce)<((fv*3)+fe):
    print('F')
elif((cv*3)+ce)==((fv*3)+fe)and(cs>fs):
    print('C')
elif((cv*3)+ce)==((fv*3)+fe)and(cs<fs):
    print('F')
else:
    print('=')