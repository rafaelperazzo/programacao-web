# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('Digite o número de vitórias do cormengo:')
ce=input('Digite o número de empates do cormengo:')
cs=input('Digite o saldo de gols do cormengo:')
fv=input('Digite o número de vitórias do flaminthias:')
fe=input('Difite o número de empates do flaminthias:')
fs=input('Digite o saldo de gols do flaminthias:')

pc=((cv*3)+(ce*1))
pf=((fv*3)+(fe*1))

if pc>pf:
    print ('C')
    if pc==pf and cs>fs:
        print ('C')
elif pf>pc:
    print ('F')
    if pf==pc and fs>cs:
        print ('F')
elif pf==pc and fs==cf:
    print ('=')