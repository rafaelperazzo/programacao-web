# -*- coding: utf-8 -*-
import math

cv=float(input('digite a vitoria do cormengo:'))
ce=float(input('digite o empate do cormengo:'))
cs=float(input('digite o saldo de gols do cormengo:'))
fv=float(input('digite a vitoria do flaminthians:'))
fe=float(input('digite o empate do flaminthians:'))
fs=float(input('digite o saldo de gols do flaminthians:'))
pc=('cv*3')+ce
pf=('cf*3')+fe


if(pc>pf):
    print('c')
elif(pc<pf):
    print('f')
else:
    print('=')
    
