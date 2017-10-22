# -*- coding: utf-8 -*-
import math

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))
n4 = int(input('Digite n4: '))

while (n1 > n2) or (n2 > n1 > n3) or (n3 > n1 > n2) or (n4 > n3) :
    if (n2 > n4) or (n4 > n2) : 
        print('''N''')        
print('S')
break