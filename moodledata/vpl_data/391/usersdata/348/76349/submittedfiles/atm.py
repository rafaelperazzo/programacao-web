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
if (((vs%20) - 10) >= 5) or (vs == 5): 
    print(1)
else:
    print(0) 
if ((vs%20) <= 14) or ((vs%20) > 15):
   x2 = (((vs%20)/2) - 5)
   print('%.d' %x2)
else:
    print(0)
    


    
    
 
    