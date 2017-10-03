# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
vs = int(input('informe o valor a ser sacado: '))

if vs >= 20 :
    x1 = vs/20
    print ('%.d' %x1)
else:
    print(0)

if ((vs%20) >= 10):
    print(1)
else:
    print(0)

if (((vs%20) - 10) >= 5) or (vs >= 5) and (vs<10): 
    print(1)
else:
    print(0) 

if  ((vs%20) - 10 >= 2) and (vs > 20) and (((vs%20) - 10) != 5):
    x2 = (((vs%20) - 10)/2)
    print ('%.d' %x2) 
elif vs == 2:
    print(1) 
elif (vs > 2) and (vs < 5): 
    x3 = (vs/2)
    print ('%.d' %x3) 
else:
    print(0)
    
 


    
    
 
    