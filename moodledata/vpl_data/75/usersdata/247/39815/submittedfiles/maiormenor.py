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
if d>b>c>d>e:
    print('%d'%a)
    print('%d'%e)
if a>b>c>d>e:
    print('%d'%a)
    print('%d'%e)
if b>c>e:
    print('%d'%b)
    print('%d'%e)
if e>b>a>c>d:
    print('%d'%e)
    print('%d'%d)
