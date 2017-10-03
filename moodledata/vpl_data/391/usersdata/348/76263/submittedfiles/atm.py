# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
vs = int(input('informe o valor a ser sacado: '))
if vs == 20:
    print (1)
    print (0)
    print (0)
    print (0)
    print (0)
elif vs == 10:
    print (0)
    print (1)
    print (0)
    print (0)
    print (0)
elif vs == 5:
    print (0)
    print (0)
    print (1)
    print (0)
    print (0)
elif vs == 2:
    print (0)
    print (0)
    print (0)
    print (1)
    print (0)
elif vs == 1:
    print (0)
    print (0)
    print (0)
    print (0)
    print (1)
if vs > 20 :
    x1 = vs/20
    print ('%.d' %x1)
if ((vs%20) > 10) or ((vs%20) == 10):
    print(1)
else:
    print(0)
if ((vs%20) ==5):
    print(1)
else:
    print(0) 

    
    
 
    