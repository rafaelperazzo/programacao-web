# -*- coding: utf-8 -*-
import math

P=int(input('1 ou 0:'))
R=int(input('1 ou 0:'))

if P==0: 
    print('C')
if P==1 and R==0:
    print('B')
if P==1 and R==1:
    print('A')