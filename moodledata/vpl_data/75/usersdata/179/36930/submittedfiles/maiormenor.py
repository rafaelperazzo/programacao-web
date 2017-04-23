# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

if a>b and b<c and c<d and d<e:
    print('a maior')
elif b>a and a<c and c<d and d<e:
    print('b maior')
elif c>a and a<b and b<d and d<e:
    print('c maior')
elif d>a and a<b and b<c and c<e:
    print('d maior')
elif e>a and a<b and b<c and c<d:
    print('e maior')
or    
if a<b and b>c and c>d and d>e:
    print('a menor')
elif b<a and a>c and c>d and d>e:
    print('a menor')
elif c<a and a>b and b>d and d>e:
    print('a menor')
elif d<a and a>b and b>c and c>e:
    print('a menor')
elif e<a and a>b and b>c and c>d:
    print('a menor')     
    

        