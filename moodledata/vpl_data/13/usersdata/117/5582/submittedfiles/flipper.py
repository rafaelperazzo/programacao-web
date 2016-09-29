# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
P=input('digite o em qual direção está a porta P:')
R=input('digite o em qual direção está a porta R:')

if P==1 and R==1:
    print('A')
if P==0:
    print('C')
if P==1 and R==0:
    print('B')