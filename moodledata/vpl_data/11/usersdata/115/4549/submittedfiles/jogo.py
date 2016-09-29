# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('digite o número de vitórias do cormengo:')
Ce=input('digite o número de empates do cormengo:')
Cs=input('digite o saldo de gols do cormengo:')
Ev=input('digite o número de vitórias do flaminthians:')
Ee=input('digite o número de empates do flaminthians:')
Es=input('digite o saldo de gols do flaminthians:')
if Cv>Ev:
    print ('C')
elif Cv<Ev:
    print ('F')
elif Cv=Ev:
    elif Ce>Ee:
        print ('C')
    elif Ce<Ee:
        print ('E')
elif Cv=Ev and Ce=Ee:
    elif Cs>Es:
        print ('C')
    elif Cs<Es:
        print ('E')