# -*- coding: utf-8 -*-
from __future__ import division
import math

a= input('insira um valor para a:')
b= input('insira um valor para b:')
c= input('insira um valor para c:')

if a<(b+c):
    print('S')
    if (a**2)==((b**2)+(c**2)):
        print('Re')
    if (a**2)>((b**2)+(c**2)):
        print('Ob')
    if (a**2)<((b**2)+(c**2)):
        print('Ac')
    if a==b and a==c:
        print('Eq')
    if b==c and c!=a:
        print('Is')
    if a!=b and b!=c:
        print('Es')
else:
    print('N')