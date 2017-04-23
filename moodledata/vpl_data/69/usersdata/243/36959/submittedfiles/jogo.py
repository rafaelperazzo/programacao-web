# -*- coding: utf-8 -*-
import math
cv=int(input('dig o n de vit do cor:'))
ce=int(input('dig o n de emp do cor:'))
cs=int(input('dig o n de saldos de gols do cor:'))
fv=int(input('dig o n de vit do fla:'))
fe=int(input('dig o n de emp do fla:'))
fs=int(input('dig o n de saldos de gols do fla:'))

v1=cv*3+ce*1
v2=fv*3+fe*1

if v1>v2:
    print('c')
elif v1<v2:
    print('c')
else:
    if cs>fs:
        print('f')
    else:
        print('=')