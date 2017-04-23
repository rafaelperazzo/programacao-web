# -*- coding: utf-8 -*-
import math
n1 = int (input('Digite o valor 1: '))
n2 = int (input('Digite o valor 2: '))
n3 = int (input('Digite o valor 3: '))
n4 = int (input('Digite o valor 4: '))

if n1==n2==n3==n4:
    print('N')
 
elif n2>n1 and n4>n3 :
    print ('N')
    
    
elif n3>n2 and n3>n4:
    print('N')
    
else:
    print('S')