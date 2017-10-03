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
if (a>b) and (a>c) and (a>d) and (a>e) and (e<b) and (e<c) and (e<d):
    print (e)
    print (a)
#a maior e d menor
elif (a>b) and (a>c) and (a>d) and (a>e) and (d<b) and (d<c) and (d<e):
    print (d)
    print (a)
#a maior e c menor
elif (a>b) and (a>c) and (a>d) and (a>e) and (c<b) and (c<d) and (c<e):
    print (a)
    print (c)
#a maior e b menor
elif (a>c) and (a>c) and (a>d) and (a>e) and (b<c) and (b<d) and (b<e):
    print (a)
    print (b)

#b maior e e menor
if (b>a) and (b>c) and (b>d) and (b>e) and (e<a) and (e<c) and (e<d):
    print (e)
    print (b)
#b maior e d menor
elif (b>a) and (b>c) and (b>d) and (b>e) and (d<a) and (d<c) and (d<e):
    print (d)
    print (b)
#a maior e c menor
elif (a>b) and (c<b) and (c<d) and (c<e):
    print (a)
    print (c)
#a maior e b menor
elif (a>c) and (b<c) and (b<d) and (b<e):
    print (a)
    print (b)