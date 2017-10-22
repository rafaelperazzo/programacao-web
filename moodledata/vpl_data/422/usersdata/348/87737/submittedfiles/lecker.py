# -*- coding: utf-8 -*-
import math

n1 = int(input( 'informe o numero 1: ')) 
n2 = int(input( 'informe o numero 2: ')) 
n3 = int(input( 'informe o numero 3: ')) 
n4 = int(input( 'informe o numero 4: ')) 

if n1 == n2 and n2 == n3 and n3 == n4 and n4 == n1:
    print( 'N')
elif n1 > n2 > n3 > n4:
    print ( 'S')
elif n1 < n2 < n3 < n4:
    print ( 'S')
elif n1 > n2 and n2 == n3 == n4:
    print('S')
elif n4 > n3 and n2 == n3 == n1:
    print('S')
elif n1 == n3 and n3 == n4 and n2 > n3 and n2 > n1:
    print ('S')
elif n1 < n2 and n2 > n3:
    print( 'N')
elif n1 == n2 and n3 > n2 and n3 > n4 and n4 == n2:
    print ('S')
elif n2 < n3 and n3 > n4:
    print( 'N')
elif n1 < n2 < n3 < n4:
    print ( 'S')
elif n1 > n2 and n2 == n3 == n4:
    print('S')
    
    
    
    
    
    
    
    
    