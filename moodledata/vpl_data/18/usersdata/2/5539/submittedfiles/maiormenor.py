# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')
c = input('Digite o número 3: ')
d = input('Digite o número 4: ')
e = input('Digite o número 5: ')

#CONTINUE...
maior = a
menor = a

#ENCONTRANDO O MAIOR

if a>=b and a>=c and a>=d and a>=e:
    if a%2==0:
        maior = a

if b>=a and b>=c and b>=d and b>=e:
    if b%2==0:
        maior = b
    
if c>=a and c>=b and c>=d and c>=e:
    if c%2==0:
        maior = c
    
if d>=a and d>=b and d>=c and d>=e:
    if d%2==0:
        maior = d

if e>=a and e>=b and e>=c and e>=d:
    if e%2==0:
        maior = e
    
#ENCONTRANDO O MENOR

if a<=b and a<=c and a<=d and a<=e:
    if a%2==0:
        menor = a

if b<=a and b<=c and b<=d and b<=e:
    if b%2==0:
        menor = b
    
if c<=a and c<=b and c<=d and c<=e:
    if c%2==0:
        menor = c
    
if d<=a and d<=b and d<=c and d<=e:
    if d%2==0:
        menor = d

if e<=a and e<=b and e<=c and e<=d:
    if e%2==0:
        menor = e
    
print ("%d" % menor)
print ("%d" % maior)

    



