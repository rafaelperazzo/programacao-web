# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite o valor a sacar: '))

n1=(n//20)
n2=(n%20)//10
n3=((n%20)%10)//5
n4=(((n%20)%10)%5)//2
n5=((((n%20)%10)%5)%2)//1

print ('%.d' %n1)
print ('%.d' %n2)
print ('%.d' %n3)
print ('%.d' %n4)
print ('%.d' %n5)
