# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a>b and a>c and a>d and a>e and b<c and b<d and b<e:
    print('%d'%b)
    print('%d'%a)
if a>b and a>c and a>d and a>e and b>c and c<d and c<e:
    print('%d'%c)
    print('%d'%a) 
if a>b and a>c and a>d and a>e and d<c and b>d and d<e:
    print('%d'%d)
    print('%d'%a)
if a>b and a>c and a>d and a>e and e<c and b>e and d>e:
    print('%d'%d)
    print('%d'%a)
if b>a and b>c and b>d and b>e and a<c and a<d and a<e:
    print('%d'%a)
    print('%d'%b)
if b>a and b>c and b>d and b>e and a>c and c<d and c<e:
    print('%d'%c)
    print('%d'%b)
if b>a and b>c and b>d and b>e and d<c and a>d and d<e:
    print('%d'%d)
    print('%d'%b)
if b>a and b>c and b>d and b>e and e<c and e<d and a>e:
    print('%d'%e)
    print('%d'%b)
if c>a and c>b and c>d and c>e and a<b and a<d and a<e:
    print('%d'%a)
    print('%d'%c)
if c>a and c>b and c>d and c>e and a>b and b<d and b<e:
    print('%d'%b)
    print('%d'%c)
if c>a and c>b and c>d and c>e and d<b and a>d and d<e:
    print('%d'%d)
    print('%d'%c)
if c>a and c>b and c>d and c>e and e<b and a>e and c<e:
    print('%d'%e)
    print('%d'%c)
if d>a and d>b and c<d and d>e and a<b and a<c and a<e:
    print('%d'%a)
    print('%d'%d)
if d>a and d>b and c<d and d>e and a>b and b<c and b<e:
    print('%d'%b)
    print('%d'%d)  
if d>a and d>b and c<d and d>e and c<b and a>c and c<e:
    print('%d'%c)
    print('%d'%d)
if d>a and d>b and c<d and d>e and e<b and e<c and a>e:
    print('%d'%e)
    print('%d'%d)
if e>a and e>b and c<e and d<e and a<b and a<c and a<d:
    print('%d'%a)
    print('%d'%e)
if e>a and e>b and c<e and d<e and a>b and b<c and b<d:
    print('%d'%b)
    print('%d'%e)
if e>a and e>b and c<e and d<e and c<b and a>c and c<d:
    print('%d'%c)
    print('%d'%e)
if e>a and e>b and c<e and d<e and d<b and d<c and a>d:
    print('%d'%d)
    print('%d'%e)


