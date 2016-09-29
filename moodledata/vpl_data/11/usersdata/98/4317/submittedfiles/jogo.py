# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('Digite o número de vitórias do cormengo: ')
ce=input('Digite o número de empates do cormengo: ')
cs=input('Digite o saldo de gols do cormengo: ')
fv=input('Digite o número de vitórias do flaminthians: ')
fe=input('Digite o número de empates do flaminthians: ')
fs=input('Digite o saldo de gols do flaminthians: ')

pc=(cv*3)+ce
pf=(fv*3)+fe

if pc>pf:
    print('C')
if pf>pc:
    print('F')
if cs>fs:
    print('C')
if fs>cs:
    print('F')
else:
    print('=')
    