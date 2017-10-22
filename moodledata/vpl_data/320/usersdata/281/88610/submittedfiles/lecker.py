# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número:  '))
b=int(input('Digite o segundo número:   '))
c=int(input('Digite o terceiro número:  '))
d=int(input('Digite o quarto número:    '))
A=0
B=0
C=0
D=0
if a>b:
    A=1
if a<b and b>c:
    B=1
if b<c and c>d:
    C=1
if d>c:
    D=1
lecker=A+B+C+D
if lecker==1
    print('S')
else:
    print('N')