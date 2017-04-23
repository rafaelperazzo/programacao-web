# -*- coding: utf-8 -*-
import math
Cv = int(input('Digite o número de vitórias do Cormengo: '))
Ce = int(input('Digite o número de empates do Cormengo: '))
Cg = int(input('Digite o saldo de gols do Cormengo: '))
Fv = int(input('Digite o número de vitórias do Flaminthians: '))
Fe = int(input('Digite o número de empates do Flaminthians: '))
Fg = int(input('Digite o saldo de gols do Flaminthians: '))

Cp = ((Cv*3)+Ce)
Fp = ((Fv*3)+Fe)

if Cp>Fp:
    print('C')
    
elif Fp>Cp:
    print('F')
    
else:
    if Cg>Fg:
        print('C')
    
    elif Fg>Cg:
        print('F')
    