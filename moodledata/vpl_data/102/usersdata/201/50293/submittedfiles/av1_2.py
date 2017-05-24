# -*- coding: utf-8 -*-
import math
n1=int(input('Digite um número:'))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número:'))
n4=int(input('Digite um número:'))
if n1==n3 and n2!=n4:
    print('V')
elif n1!=n3 and n2==n4:
    print('V')
else:
    print('F')