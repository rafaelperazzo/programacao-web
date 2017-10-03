# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor = int(input('digite o valor que deseja sacar:'))
a=20
b=10
c=5
d=2
e=1
t=valor%a
u=t%b
v=u%c
x=v%d
z=x%e
if t==0 :
    f=(valor//a)
    print('%.d'%f)
    print(0)
    print(0)
    print(0)
    print(0)
elif f==0 :
    print(0)
elif t!=0 and u==0 :
    f=(valor//a)
    g=(t//b)
    print('%.d'%f)
    print('%.d'%g)
    print(0)
    print(0)
    print(0)
elif f==0 or g==0 :
    print(0)
elif t!=0 and u!=0 and v==0 :
    f=(valor//a)
    g=(t//b)
    h=(u//c)
    print('%.d'%f)
    print('%.d'%g)
    print('%.d'%h)
    print(0)
    print(0)
elif f==0 or g==0 or h==0 :
    print(0)
elif t!=0 and u!=0 and v!=0 and x==0 :
    f=(valor//a)
    g=(t//b)
    h=(u//c)
    i=(v//d)
    print('%.d'%f)
    print('%.d'%g)
    print('%.d'%h)
    print('%.d'%i)
    print(0)
else:
    f=(valor//a)
    g=(t//b)
    h=(u//c)
    i=(v//d)
    j=(x//e)
    print('%.d'%f)
    print('%.d'%g)
    print('%.d'%h)
    print('%.d'%i)
    print('%.d'%j)

    
    