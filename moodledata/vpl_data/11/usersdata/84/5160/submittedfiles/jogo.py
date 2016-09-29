# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('numero de vitorias do cormengo:')
Ce=input('numero de empates do cormengo:')
Cs=input('saldo de gols do cormengo:')
Fv=input('numero de vitorias do flaminthians:')
Fe=input('numero de empates do flaminthians:')
Fs=input('saldo de gols do flaminthians:')

t1=(Cv*3)+(Ce*1)+Cs
t2=(Fv*3)+(Fe*1)+Fs

if(t1>t2):
    print('C')
    
if(t2>t1):
    print('F')
    
if(t2==t1):
    print('=')
    
