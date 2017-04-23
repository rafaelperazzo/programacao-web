# -*- coding: utf-8 -*-
cv=int(input('quantidade de vitorias do cormengo'))
ce=int(input('quantidade de empates do cormengo'))
cs=int(input('saldo de gols do cormengo'))
fv=int(input('quantidade de vitorias do flaminthias'))
fe=int(input('quantidade de empates do flaminthias'))
fs=int(input('saldo de gols do flaminthias'))
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