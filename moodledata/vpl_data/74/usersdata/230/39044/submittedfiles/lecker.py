# -*- coding: utf-8 -*-
import math
n1=float(input('Digite primeiro número: '))
n2=float(input('Digite segundo número: '))
n3=float(input('Digite terceiro número: '))
n4=float(input('Digite quarto número: '))
if n2>n1 and n2>n3 and n4>n3: 
    print('N')
elif n1>n2 and n4>n3:
    print('N')
elif n3>n4 and n3>n2 and n1>n2:
    print('N')
elif n2>n1 and n2<n3 or n3>n2 and n3>n4:
    print('S')
elif n1>n2 and n4>n3:
    print('S')
else:
    print('N')
    