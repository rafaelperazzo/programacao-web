# -*- coding: utf-8 -*-
import math
cv=int(input('digite o numero de vitoria do cormengo:'))
ce=int(input('digite o numero de empates do cormengo:'))
cs=int(input('digite o numero do saldo de gols do cormengo:'))
fv=int(input('digite o numero de vitoria do flaminthians:'))
fe=int(input('digite o numero de empates do flaminthians:'))
fs=int(input('digite o numero do saldo de gols do flaminthians:'))
pc=(cv*3)+(ce*1)
pf=(fv*3)+(fe*1)
if pc>pf:
    print('C')
elif pc<pf:
    print('F')
elif pc==pf:
    if cs>fs:
        print('C')
    elif cs<fs:
        print('F')
else:
    print('=')