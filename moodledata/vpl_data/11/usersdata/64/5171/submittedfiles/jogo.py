# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input('Digite o número de vitótias do Cormengo: ')
Ce = input('Digite o número de empates do Cormengo: ')
Cs = input('Digite o saldo de gols: ')
Fv = input('Digite o número de vitótias do Flaminthians: ')
Fe = input('Digite o número de empates do Flaminthians: ')
Fs = input('Digite o saldo de gols: ')




if Cv > Fv:
    print "'C'"
elif Cv < Fv:
    print "'F'"
elif Cv == Fv:
    if Cs > Fs:
        print "'C'"
    elif Cs < Fs:
        print "'F'"
        
        if Ce > Fe:
            print "'C'"
        elif Ce < Fe:
            print "'V'"
else: 
    print "'='"
    
    
    
