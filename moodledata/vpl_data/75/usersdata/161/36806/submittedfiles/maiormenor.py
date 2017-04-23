# -*- coding: utf-8 -*-
import math

a = int(input('Digite o número 1: '))
b = int(input('Digite o número 2: '))
c = int(input('Digite o número 3: '))
d = int(input('Digite o número 4: '))
e = int(input('Digite o número 5: '))
maior=0
menor=0
if a>maior:
    maior=a
elif b>maior:
    maior=b
elif c>maior:
    maior=c
elif d>maior:
    maior=d
elif e>maior:
    maior=e
if a<menor:
    menor=a
elif b<menor:
    menor=b
elif c<menor:
    menor=c
elif d<menor:
    menor=d
elif e<menor:
    menor=e
print(maior)
print(menor)