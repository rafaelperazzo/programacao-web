# -*- coding: utf-8 -*-
from __future__ import division
import math

valor= float(input('Digite o valor a ser sacado: '))
if valor%20==0:
    print(valor//20)
    if valor%20!=0:
        print(0)
    valor= valor - valor%20
elif valor%10==0:
    print(valor//10)
    if valor%10!=0:
        print(0)
    valor= valor - valor%10
elif valor%5==0:
    print(valor//5)
    if valor%5!=0:
        print(0)
    valor=valor - valor%5
elif valor%2==0:
    print(valor//2)
    if valor%2!=0:
        print(0)
else:
    print(valor//1)