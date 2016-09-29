# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=int(input("digite as vitorias:"))
Ce=int(input("digite os empates:"))
Cs=int(input(" digite o saldo:"))
Fv=int(input("digite as vitorias:"))
Fe=int(input("digite os empates:"))
Fs=int(input("digite o saldo:"))
Pc=(Cv*3)+(1*Ce)
Pf=(Fv*3)+(1*Fe)
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