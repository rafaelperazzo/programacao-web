# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor_inteiro=int(input("Digite seu valor: "))
c20= valor_inteiro//20
c10= c20%20//10
c5= c10%10
c2= c5%5//2
c1= c2%2//1
print('%d' % c20)
print('%d' % c10)
print('%d' % c5)
print('%d' % c2)
print('%d' % c1)