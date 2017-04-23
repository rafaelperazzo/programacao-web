# -*- coding: utf-8 -*-
import math
Cv=float(input('numero de vitorias:'))
Ce=float(input('numero de empates:'))
Cs=float(input('saldo de gols:'))
Fv=float(input('numero de vitorias:'))
Fe=float(input('numero de empates:'))
Fs=float(input('saldo de gols:'))

v=3
e=1

if (v*Cv+e*Ce)>(v*Fv+e*Fe) and Cs>Fs:
    prin('C')