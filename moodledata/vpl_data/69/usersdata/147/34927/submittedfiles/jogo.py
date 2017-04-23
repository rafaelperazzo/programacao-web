# -*- coding: utf-8 -*-
import math
Cv=int(input('digite vitórias de c:'))
Ce=int(input('digite empates de c:'))
Cs=int(input('digite saldo de gols de c:'))
Fv=int(input('digite vitórias de f:'))
Fe=int(input('digite empates de f:'))
Fs=int(input('digite saldo de gols de f:'))

#Pontos de vitórias do C#
Pcv=Cv*3
#Pontos de empates do C#
Pce=Ce*1
#Pontos de vitórias do F#
Pfv=Fv*3
#Pontos de empates do F#
Pfe=Fe*1
if Pcv>Pfv and Cs>Cf:
    print('C')
if Pcv<Pfv and Cs<Cf:
    print('F')
if (Pcv+Pce)==(Pfe+Pfv) and Fs>Cs:
    print('F')
if (Pcv+Pce)==(Pfe+Pfv) and Fs<Cs:
    print('C')