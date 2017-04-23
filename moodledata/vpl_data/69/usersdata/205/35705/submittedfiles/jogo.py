# -*- coding: utf-8 -*-
import math

cv=float(input('digite a vitoria do cormengo:'))
ce=float(input('digite o empate do cormengo:'))
cs=float(input('digite o saldo de gols do cormengo:'))
fv=float(input('digite a vitoria do flaminthians:'))
fe=float(input('digite o empate do flaminthians:'))
fs=float(input('digite o saldo de gols do flaminthians:'))

if(cv>fv):
    print('c')
elif(cv<fv):
    print('f')
else:
    print('=')
    
