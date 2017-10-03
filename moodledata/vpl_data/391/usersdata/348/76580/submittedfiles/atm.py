# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
vs = int(input('informe o valor a ser sacado: '))
#conta para o 20
if vs >= 20 :
    x1 = vs//20
    vs -= x1*20 
    print ('%.d' %x1)
else:
    print(0)

# conta para o 10
if (vs >= 10):
    x1 = vs//10
    vs -= x1*10 
    print ('%.d' %x1)
else:
    print(0)

# conta do 5 
if (vs >= 5): 
    x1 = vs//5
    vs -= x1*5
    print ('%.d' %x1)
else:
    print(0) 

# conta para 2 (vs > 20) and
if (vs >= 2): 
    x1 = vs//2
    vs -= x1*2
    print ('%.d' %x1)
else:
    print(0)

#calcular 1
if (vs >= 1): 
    vs -= x1
    print ('%.d' %x1)
else:
    print(0)    
    
 


    
    
 
    