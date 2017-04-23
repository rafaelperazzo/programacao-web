# -*- coding: utf-8 -*-
import math
cv=float(input('digite vitórias do cormengo:'))
ce=float(input('digite empates do cormengo:'))
cs=float(input('digite o saldo dos gols do cormengo:'))
fv=float(input('digite vitórias do flaminthians:'))
fe=float(input('digite empates do fleminthians:'))
fs=float(input('digite o saldo dos gols do flaminthians:'))
if((cv*3)+ce)>((fv*3)+fe):
    print('c')
elif((cv*3)+ce)<((fv*3)+fe):
    print('f')
elif((cv*3)+ce)==((fe*3)+fe)and(cs>fs):
    print('c')
elif((cv*3)+ce)==((fv*3)+fe)and(cs<fs):
    print('f')
else:
    print('=')
    