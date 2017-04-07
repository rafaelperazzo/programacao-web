# -*- coding: utf-8 -*-
from __future__ import division
import math
v=int(input('Digite o Valor:'))
q20=v//20 
q10=(v%20)//10
q5=((v%20)%10)//5
q2=(((v%20)%10)%5)//2
q1=((((v%20)%10)%5)%2)//1
print ('%d' %q20)
print ('%d' %q10)
print ('%d' %q5)
print ('%d' %q2)
print ('%d' %q1)