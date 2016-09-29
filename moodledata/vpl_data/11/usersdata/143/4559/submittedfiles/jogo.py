# -*- coding: utf-8 -*-
from __future__ import division
import math
cv = input(' Numero de vitórias do Cormengo: ')
ce = input(' Numero de empates do Cormengo: ')
cs = input(' Saldo de gols do Cormengo: ')
fv = input(' Numero de vitórias do Flaminthians: ')
fe = input(' Numero de empates do Flaminthians: ')
fs = input(' Saldo de gols do Flaminthians: ')

pc = 3*cv+ce
pf = 3*fv+fe

if pc>pf:
    print(' C ')
elif pc<pf:
    print(' F ')
else:
    if cs>fs:
        print(' C ')
    elif cs<fs:
        print(' F ')
    else:
        print(' = ')
        
    
    
    
    
    
    
    
    
    
    