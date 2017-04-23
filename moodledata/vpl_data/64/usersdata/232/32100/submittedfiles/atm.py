# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Digite o valor do saque: '))
n=(valor/20)
x=((valor%20)/10)
y=(((valor%20)%10)/5)
z=((((valor%20)%10)%5)/2)
h=(((((valor%20)%10)%5)%2)/1)
if valor%20==0:
    print('%d' %n)
    print('%d' %x)
    print('%d' %y)
    print('%d' %z)
    print('%d' %h)
if valor%20!=0 and valor%10==0:
    print('%d' %n)
    print('%d' %x)
    print('%d' %y)
    print('%d' %z)
    print('%d' %h)
if valor%10!=0 and valor%5==0:
    print('%d' %n)
    print('%d' %x)
    print('%d' %y)
    print('%d' %z)
    print('%d' %h)