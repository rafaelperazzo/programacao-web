# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
t1 = int(input('insira o numero de tomadas na primeira regua:'))
t2 = int(input('insira o numero de tomadas na segunda regua:'))
t3 = int(input('insira o numero de tomadas na terceira regua:'))
t4 = int(input('insira o numero de tomadas na quarta regua:'))
tomadas = ((t1-1) + (t2-1) + (t3-1) + t4)
if t1>1 and t2>1 and t3>1 and t4>1:
    print ('%d' %tomadas)