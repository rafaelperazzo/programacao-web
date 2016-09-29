# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input(' digite o numero de vitórias do cormengo:')
b=input('digite o numero de empates do cormengo:')
c= input('digite o numero do saldo de gols do cormengo:')
d=input(' digite o numero de vitorias do flaminthias:')
e=input(' digite o numero de empates do flaminthias:')
f=input(' digite o numero do saldo de gols flaminthias:')
x= (a*3)+(b*1)
y= (d*3)+(e*1)
if x>y:
    print('c')
if x<y:
    print('f')
if x==y and c==f:
    print('=')