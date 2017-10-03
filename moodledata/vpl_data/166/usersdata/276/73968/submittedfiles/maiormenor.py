# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
#menor 
#maior
#a maior e e menor
if (a>b) and (b>=c) and (c>=d) and (d>e):
    print (e)
    print (a)
#a maior e d menor
elif (a>b) and (b>=c) and (c>=e) and (e>d):
    print (d)
    print (a)
#a maior e c menor
elif (a>b) and (b>=d) and (d>=c) and (e>c):
    print (a)
    print (c)

