# -*- coding: utf-8 -*-
import math

P=int(input('digite a posição da porta P:'))
R=int(input('digite a posição da porta R:'))
if P==0:
    if R==1 or R==0:
        print('C')
if P==1:
    if R==1:
        print ('A')
    if R==0:
        print ('B')
