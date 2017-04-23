# -*- coding: utf-8 -*-
import math
cv=int(input('digite o numero de vitorias do cormengo:'))
ce=int(input('digite o numero de empates do cormengo:'))
cg=int(input('digite o numero de gols do cormengo:'))
fv=int(input('digite o numero de vitorias do flaminthians:'))
fe=int(input('digite o numero de empates do flaminthians:'))
fg=int(input('digite o numero de gols do flaminthians:'))
pc=3*cv+ce
pf=3*fv+fe
if pc>pf:
    print('c')
elif pc<pf:
    print('f')
else:
    if cg>fg:
        print('c')
    elif cg<fg:
        print('f')
    else:
        print('=')