# -*- coding: utf-8 -*-
import math
v1 = float(input('Vitorias do Cormengo:'))
e1 = float(input('Empates do Cormengo:'))
s1 = float(input('Saldo de gols do Cormengo:'))
v2 = float(input('Vitorias do Flaminthians:'))
e2 = float(input('Empates do Flaminthians:'))
s2 = float(input('Saldo de gols do Flaminthians:'))
t1 = (v1*3)+e1
t2 = (v2*3)+e2
if t1>t2:
    print('C')
elif t1<t2:
    print('F')
else:
    if t1==t2 and s1>s2:
        print('C')
    elif t1==t2 and s1<s2:
        print('F')
    else:
        print('=')