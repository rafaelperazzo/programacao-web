# -*- coding: utf-8 -*-
from __future__ import division
import math

P= input('Insira a posição de P:')
R= input('Insira a posição de R:')

if P==0:
    print('C')
if P==1:
    if R==0:
        print('B')
    if R==1:
        print('A')