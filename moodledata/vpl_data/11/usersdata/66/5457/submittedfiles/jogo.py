# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input("digite as vitorias:")
Ce=input("digite os empates:")
Cs=input(" digite o saldo:")
Fv=input("digite as vitorias:")
Fe=input("digite os empates:")
Fs=input("digite o saldo:")
Pc=(Cv*3)+(1*Ce)
Pf=(fV*3)+(1*Fe)
if Pc>Pf:
    print("C")
if Pf>Pc:
    prnit("F")
if (Pc==Pf) and (Cs>Fs):
    print("C")
if (Pc==Pf) and (Fs>Cs):
    print("F")
if (Pc==Ps) and (Cs==Fs):
    print("=")