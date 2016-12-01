# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite o número de salas:')
e = input ('Digite a porta de entrada:')
s = input ('Digite a porta de saída:')

l = []
for i in range (0,n,1):
    l.append ('Digite a quantidade de vidas:')

if (e==s):
    print l[e]
