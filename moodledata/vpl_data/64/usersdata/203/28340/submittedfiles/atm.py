# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor_inteiro=int(input("Digite seu valor: "))
c20= valor_inteiro//20
r20= valor_inteiro%20
c10= r20//10
r10= r20%10
c5= r10//5
r5= r10%5
c2= r5//2
r2= r5%2
c1= r2//1
print('%d' % c20)
print('%d' % c10)
print('%d' % c5)
print('%d' % c2)
print('%d' % c1)