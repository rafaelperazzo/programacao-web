# -*- coding: utf-8 -*-
from __future__ import division
import math

#Entrda

n1 = float(input('Digite valor de "n1": '))
n2 = float(input('Digite valor de "n2": '))
n3 = float(input('Digite valor de "n3": '))
n4 = float(input('Digite valor de "n4": '))

#Processamento

if n1 > n2:
    print('S')
    
elif ((n2) > (n3)) and ((n2) > (n1)):
    print('S')
    
elif ((n3) > (n4))  and ((n3) > (n2)):
    print('S')
    
elif ((n4) > (n3)):
    print('S')
    
elif (n1 > n2) and (n4 > n3):
    print('N')

elif (n2 > n1)  and (n2 > n3) and (n4 > n3):
    print('N')

elif (n3 > n2) and (n3  >  n4):
    print('N')
    
elif  (n4 > n3) and (n1 > n2):
    print('N')

else:
    print('N')
        

