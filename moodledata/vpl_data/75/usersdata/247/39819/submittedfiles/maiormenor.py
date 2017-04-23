# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a>b>c>d>e:
    print('%d'%a)
    print('%d'%e)
if d>b>c>a>e:
    print('%d'%a)
    print('%d'%e)
if a>b>c>d>e:
    print('%d'%a)
    print('%d'%e)
if b>c>e:
    print('%d'%e)
    print('%d'%b)
if e>b>a>c>d:
    print('%d'%d)
    print('%d'%e)
else:
    print('%d'%a)
    print('%d'%a)