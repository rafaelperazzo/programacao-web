# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor de c: '))
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)==((b**2)+(c**2)))and((a==b)(b==c)):
    print('S')
    print('Re')
    print('Eq')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)==((b**2)+(c**2)))and((b==c)(c=!a)):
    print('S')
    print('Re')
    print('Is')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)==((b**2)+(c**2)))and((a=!b)(b=!c)):
    print('S')
    print('Re')
    print('Es')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)>((b**2)+(c**2)))and((a==b)(b==c)):
    print('S')
    print('Ob')
    print('Eq')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)>((b**2)+(c**2)))and((b==c)(c=!a)):
    print('S')
    print('Ob')
    print('Is')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)>((b**2)+(c**2)))and((a=!b)(b=!c)):
    print('S')
    print('Ob')
    print('Es')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)<((b**2)+(c**2)))and((a==b)(b==c)):
    print('S')
    print('Ac')
    print('Eq')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)<((b**2)+(c**2)))and((b==c)(c=!a)):
    print('S')
    print('Ac')
    print('Is')
if((a>=b)(b>=c)(c>0))and(a<(b+c))and((a**2)<((b**2)+(c**2)))and((a=!b)(b=!c)):
    print('S')
    print('Ac')
    print('Es')
else:
    print('N')