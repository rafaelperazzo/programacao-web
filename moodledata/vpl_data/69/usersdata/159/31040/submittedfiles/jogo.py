# -*- coding: utf-8 -*-
import math
cv=int(input('Número de vitórias do Cormengo:'))
ce=int(input('Número de empates do Cormengo:'))
cs=int(input('Saldo de gols do Cormengo:'))
fv=int(input('Número de vitórias do Flaminthians:'))
fe=int(input('Número de empates do Flaminthians:'))
fs=int(input('Saldo de gols do Flaminthians:'))
pontosc=(3*cv)+ce
pontosf=(3*fv)+fe
if pontosc>pontosf:
    print('C')
elif pontosc<pontosf:
    print('F')
else:
    if cs>fs:
     print('C')
    if cs<fs:
        print('F')
    else:
        print('=')