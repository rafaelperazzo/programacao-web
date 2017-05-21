# -*- coding: utf-8 -*-
a=float(input('digite a váviavel que acompanha x ao quadrado:'))
b=float(input('digite a váriavel que acompanha x:'))
c=float(input('digite o termo independente:'))
delta=(b*b)-(4*a*c)
if delta >=0:
    x1=(-b+(delta**(1/2)))/2*a
    x2=(-b-(delta**(1/2)))/2*a
    print('%1f'%x1)
    prit('%1f'%x2)
else:
    print('a equação não tem raízes')