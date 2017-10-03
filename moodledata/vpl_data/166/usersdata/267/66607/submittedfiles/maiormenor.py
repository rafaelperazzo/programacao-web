# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))

#CONTINUE...
if a<b:
    menor=a
    maior=b
else:
    menor=b
    maior=a
if menor>c:
    menor=c
if menor>d:
    menor=d
if menor>e:
    menor=e
if maior<c:
    maior=c
if maior<d:
    maior=d
if maior<e:
    maior=e
print('Menor: %d' %menor)
print('Maior: %d' %maior)
