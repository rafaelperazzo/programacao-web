# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o valor do número 1: '))
n2=int(input('Digite o valor do número 2: '))
n3=int(input('Digite o valor do número 3: '))
n4=int(input('Digite o valor do número 4: '))
if n1!=n3 and n2==n3 or n1==n3 and n2!=n4:
    print('V')
if n1==n4 and n2!=n3 or n1!=n4 and n2==n3:
    print('F')

