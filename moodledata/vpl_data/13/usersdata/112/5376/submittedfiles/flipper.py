# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO AQUI
P=input('Digite 1 ou 0 para a posição da portinha:')
R=input('Digite 1 ou 0 para a posição da portinha:')


if P==0:
    print('C')
if P==1 and R==0:
    print('B')
if P==1 and R==1:
    print('A')