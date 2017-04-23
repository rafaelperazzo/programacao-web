# -*- coding: utf-8 -*-
import math

Cv= int(input('digite o numero de vitorias do cormengo:'))
Ce= int(input('digite o numero de empates do cormengo:'))
Cg= int(input('digite saldo de gols do cormengo:'))
Fv= int(input('digite o numero de vitorias do flaminthias:'))
Fe= int(input('digite o numero de empates do flaminthias:'))
Fg= int(input('digite o saldo de gols do flaminthias:'))

Cp=(Cv*3)+(Ce*1)
Fp=(Fv*3)+(Fe*1)

if Cp>Fp:
    print('C')
elif Fp>Cp:
    print('F')
else:
    if Cg>Fg:
        print('C')
    elif Fg>Cg:
        print('F')
    else:
        print('=')