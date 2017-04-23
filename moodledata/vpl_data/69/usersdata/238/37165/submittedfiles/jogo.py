# -*- coding: utf-8 -*-
cv=int(input('digite a quantidade de vitorias do cormengo:'))
ce=int(input('digite a quantidade de empates do cormnego:'))
cs=int(input('digite o saldo de gols do cormengo:'))
fv=int(input('digite a quantidade de vitorias do flaminthians:'))
fe=int(input('digite a quantidade de empates do flaminthians:'))
fs=int(input('digite o saldo de gols do flaminthinas:'))
pc=(cv*3)+ce
pf=(fv*3)+fe
if pc>pf:
    print('c')
elif pf>pc:
    print('f')
else:
    if cs>fs:
        print('c')
    elif fs>cs:
        print('f')
    else:
        print('=')
        
