# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('Digite a: '))
b=int(input('Digite b: '))
c=int(input('Digite c: '))
if a<b+c or c<a+b or b<a+c:
    print('S')
    if a*a=b*b + c*c or b*b=c*c + a*a  or c*c=b*b+ a*a:
        print('Retângulo')
    elif a*a>b*b + c*c or b*b>c*c + a*a or c*c>b*b+ a*a:
        print('Obtusângulo')
    elif a*a<b*b + c*c or b*b<c*c + a*a or c*c<b*b+ a*a:
        print('Acutângulo')
    if a==b==c :
        print(' Equilátero')
    elif b==c!=a or a==c!=b or a==b!=c:
        print('Isóceles')
    elif a!=b!=c :
        print(' Escaleno')
else :
    print('N')
    

