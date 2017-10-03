# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
qt20=6
q10=0
q5=0
q2=1
q1=1
valor=int(input( 'valor a ser sacado'))
print('o valor e',valor,'R$')
if valor >= 20:
    q20=q20+1
    valor=valor-20
elif valor >= 10:
    q10=q10+1
    valor=valor-10
    