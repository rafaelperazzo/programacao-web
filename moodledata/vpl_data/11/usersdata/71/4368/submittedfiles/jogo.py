# -*- coding: utf-8 -*-
from __future__ import division
import math

cv = input("Nº de Vitórias do Cormengo: ")
ce = input("Nº de Empate do Cormengo: ")
cs = input("Saldo de Gol do Cormengo: ")
fv = input("Nº de Vitórias do Flaminthians: ")
fe = input("Nº de Empate do Flaminthians: ")
fs = input("Saldo de Gol do Flaminthians: ")

pc = (cv*3+ce)
pf = (fv*3+fe)

if pc>pf:
    print("C")
elif pf>pc:
    print("F")
else:
    if cs>cf:
        print("C")
    elif cf>cs:
        print("F")
    elif cs==fs:
        print("=")