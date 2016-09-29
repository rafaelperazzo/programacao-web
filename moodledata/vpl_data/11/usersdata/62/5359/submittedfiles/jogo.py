# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA

cv=input("Numero de vitorias do Cormengo: ")
ce=input("Numero de empates do Cormengo: ")
cs=input("Saldo de gols do Cormengo: ")
fv=input("Numero de vitorias do Flaminthians: ")
fe=input("Numero de empates do Flaminthians: ")
fs=input("Slado de gols do Flaminthians: ")

#PROCESSAMENTO

pontosC=cv*3+ce
pontosF=fv*3=fe

#SAIDA

if pontsC>pontosF:
    print("C")
else:
    if pontosF>pontosC:
        print("F")
    else:
        if cs>fs:
            print("C")
        else:
            if fs>cs:
                print("F")
            else:
                print("=")

