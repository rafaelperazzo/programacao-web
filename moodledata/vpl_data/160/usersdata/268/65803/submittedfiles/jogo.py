# -*- coding: utf-8 -*-
import math

Cv=int(input(' Vitorias: '))
Ce=int(input(' Empates: '))
Cs=int(input(' Saldo de Gols: '))

Fv=int(input(' Vitorias: '))
Fe=int(input(' Empates: '))
Fs=int(input(' Saldo de Gols: '))

if ((Cv*3) + Ce)>(Fv*3) + Fe):
    print('C')
elif ((Cv*3) + Ce)<(Fv*3) + Fe):
    print('F')
elif (Cs>Fs):
    print('C')
elif (Cs<Fs):
    print('F')
else:
    print('=')