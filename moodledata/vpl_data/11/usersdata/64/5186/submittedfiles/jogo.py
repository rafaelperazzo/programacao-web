# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input('Digite o número de vitótias do Cormengo: ')
Ce = input('Digite o número de empates do Cormengo: ')
Cs = input('Digite o saldo de gols: ')
Fv = input('Digite o número de vitótias do Flaminthians: ')
Fe = input('Digite o número de empates do Flaminthians: ')
Fs = input('Digite o saldo de gols: ')

C = (Cv * 3) + Ce
F = (Fv * 3) + Fe


if C > F:
    print "'C'"
elif C < F:
    print "'F'"
elif C == F:
    if Cs > Fs:
        print "'C'"
    elif Cs < Fs:
        print "'F'"
    elif Cs == Fs:
        if Ce > Fe:
            print "'C'"
        elif Ce < Fe:
            print "'V'"
        
else: 
    print "'='"
    
    
    
