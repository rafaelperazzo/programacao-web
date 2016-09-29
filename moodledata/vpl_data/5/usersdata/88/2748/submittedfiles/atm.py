# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite o valor a sacar: ')

n20=(n//20)
n10=(n%20)//10
n5=((n%20)%10)//5
n2=(((n%20)%10)%5)//2
n1=((((n%20)%10)%5)%2)//1

print ('%.d' %n20)
print ('%.d' %n10)
print ('%.d' %n5)
print ('%.d' %n2)
print ('%.d' %n1)
