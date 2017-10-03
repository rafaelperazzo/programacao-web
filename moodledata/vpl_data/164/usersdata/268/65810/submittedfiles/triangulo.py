# -*- coding: utf-8 -*-
import math

a= int(input('Digite o lado a '))
b= int(input('Digite o lado b '))
c= int(input('Digite o lado c '))

if (a> b + c) or (a = b + c):
    print('N')
if (a< b+c):
    print('S')
    
    