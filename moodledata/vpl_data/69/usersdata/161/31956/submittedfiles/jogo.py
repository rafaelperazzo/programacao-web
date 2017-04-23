# -*- coding: utf-8 -*-
import math
Cv=int(input('Informe o número de vitórias:'))
Ce=int(input('Informe o número de empates:'))
Cs=int(input('Informe o saldo de gols:'))
Fv=int(input('Informe o número de vitórias:'))
Fe=int(input('Informe o número de empates:'))
Fs=int(input('Informe o saldo de gols:'))
v=3
e=1
v*Cv=Vc
Ce*e=Ec
Fv*v=Vf
Fe*e=Ef
if Vc+Ec>Vf+Ef:
    print('C')
elif Vf+Ef>Vc+Ec:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
    else:
        ('=')