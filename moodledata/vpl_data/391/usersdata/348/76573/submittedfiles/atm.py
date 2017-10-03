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
    x1 = vs//10
    vs -= x1*10 
    print ('%.d' %x1)
else:
    print(0) 

# conta para 2 (vs > 20) and
if  (((vs%20) - 15) >= 2) and (((vs%20) - 10) != 5):
    x2 = (((vs%20) - 10)/2)
    print ('%.d' %x2) 
elif vs == 2:
    print(1) 
elif (vs > 2) and (vs < 5): 
    x3 = (vs/2)
    print ('%.d' %x3) 
elif (vs > 5) and ( vs < 10) and ( vs != 6): 
    x4 = ((vs - 5)/2)
    print ('%.d' %x4)
else:
    print(0)

#calcular 1
if (vs == 1) or ((3>=vs <= 6) and ( vs!= 5)  and (vs != 4)): 
    print(1)
elif  (((vs%20) - 15) >= 1):
    print(1)
else:
    print(0)    
    
 


    
    
 
    