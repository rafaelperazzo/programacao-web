# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
if a>=b>=c>=d>=e:
    print('a')
    if b<=a<=c<=d<=e:
        print('b')
    if c<=a<=b<=d<=e:
        print('c')
    if d<=a<=b<=c<=e:
        print('d')
    else:
        print('e')
if b>=a>=c>=d>=e:
    print('b')
    if a<=b<=c<=d<=e:
        print('a')
    if c<=a<=b<=d<=e:
        print('c')
     if d<=a<=b<=c<=e:
        print('d')
    else:
        print('e')
if c>=a>=b>=d>=e:
    print('e')
    if a<=b<=c<=d<=e:
        print('a')
    if b<=a<=c<=d<=e:
        print('b')
     if d<=a<=b<=c<=e:
        print('d')
    else:
        print('e')
if d>=a>=b>=c>=e:
    print('d')
    if a<=b<=c<=d<=e:
        print('a')
    if b<=a<=c<=d<=e:
        print('b')
     if c<=a<=b<=d<=e:
         print('c')
    else:
        print('e')
if e>=a>=b>=c>=d:
    print('e')
    if a<=b<=c<=d<=e:
        print('a')
    if b<=a<=c<=d<=e:
        print('b')
     if c<=a<=b<=d<=e:
         print('c')
    else:
        print('d')