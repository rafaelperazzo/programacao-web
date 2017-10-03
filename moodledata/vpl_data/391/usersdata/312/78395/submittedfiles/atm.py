# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
q20=6
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
elif valor >= 5:
    q5=q5+1
    valor=valor-5
elif valor >= 2:
    q2=q2+1
    valor=valor-2
elif valor >= 1:
    q1=q1+1
    valor=valor-1
print('a quantidade de notas de 20 e',q20,'q10 e',q10,'q5 e',q5,'q2 e',q2,'q1 e',q1)




    