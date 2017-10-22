# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
d=int(input('Digite o quarto valor: '))
A=0
B=0
C=0
D=0
if a>b:
    A=1
if b>a or b>c:
    B=1
if c>b or c>d:
    C=1
if d>c:
    D=1
lecker=A+B+C+D
if lecker==1:
    print('S')
else:
    print('N')