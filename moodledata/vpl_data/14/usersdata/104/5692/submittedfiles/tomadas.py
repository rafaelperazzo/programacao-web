# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
t1=int(input('Digite o número de tomadas da primeira régua:'))
t2=int(input('Digite o número de tomadas da segunda régua:'))
t3=int(input('Digite o número de tomadas da terceira régua:'))
t4=int(input('Digite o número de tomadas da quarta régua:'))
#PROCESSAMENTO
tomadas=((((((t1-1)+t2)-1)+t3)-1)+t4)
#SAÍDA
print('%.i'%(tomadas))
