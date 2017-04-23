# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))
n3=int(input('digite o terceiro numero:'))
n4=int(input('digite o quarto numero:'))
if n1>n2 and n3<n2 and n4<n3:
    print('S')
    if n2>n1 and n2>n3 and n3<n3:
        print('S')
    elif n3>n2 and n3>n4 and n1<n2:
        print('S')
    elif n4>n3 and n3<n2 and n1<n2:
        print('S')
else:
    print('N')

