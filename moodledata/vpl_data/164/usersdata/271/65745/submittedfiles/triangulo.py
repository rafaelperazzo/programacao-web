# -*- coding: utf-8 -*-
import math
#ENTRADA
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))
#PROCESSAMENTO
if a<(b+c) :
    print('S')
else :
    print('N')
if a<(b+c) and (a*a)==(b*b)+(c*c) :
    print('Re')
if a<(b+c) and (a*a)>(b*b)+(c*c) :
    print('Ob')
if a<(b+c) and (a*a)<(b*b)+(c*c) :
    print('Ac')
if a<(b+c) and a==b==c:
    print('Eq')
if a<(b+c) and b==c!=a:
    print('Is')
    
