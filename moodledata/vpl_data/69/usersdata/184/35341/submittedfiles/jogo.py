# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitórias do cormengo:'))
Ce=int(input('digite o número de empates do cormengo:))
Cs=int(input('digite o saldo de gols do cormengo:'))
Fv=int(input('digite o número de vitórias do flaminthians:'))
Fe=int(input('digite o número de empates do flaminthians:'))
Fs=int(input('digite o saldo de gols do flaminthians:'))
pontoscormengo=(3*cv)+(1*ce)
pontosflaminthians=(3*fv)+(1*fe)
if pontoscormengo>pontosflaminthians:
    print('C')
elif pontosflaminthias>pontoscormengo:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
    else:
        print('=')