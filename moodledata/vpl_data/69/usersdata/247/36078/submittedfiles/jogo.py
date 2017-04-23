# -*- coding: utf-8 -*-
import math
cv=int(input('numero de vitorias de c: '))
ce=int(input('numero de empates de c: '))
cs=int(input('saldo de gols de c: '))
fv=int(input('numero de vitorias de f: '))
fe=int(input('numero de empates de f: '))
fs=int(input('saldo de gols de f: '))
cp=(cv*3)+(ce*1)
fp=(fv*3)+(fe*1)
if cp>fp:
    