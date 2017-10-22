 # -*- coding: utf-8 -*-
import math
n1= int(input('Insira o primeiro número: '))
n2= int(input('Insira o segundo número: '))
n3= int(input('Insira o terceiro número: '))
n4= int(input('Insira o quarto número: '))
c=0
if n1>n2:
    c=c+1
if n2>n1 and n2>n3:
    c=c+1
if n3>n2 and n3>n4:
    c=c+1
if n4>n3:
    c=c+1
if c==1:
    print('S')
if c>1 or c==0:
    print('N')

