# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite o valor a sacar: ')

n01=(n//20)
n02=(n%20)//10
n03=((n%20)%10)//5
n04=(((n%20)%10)%5)//2
n05=((((n%20)%10)%5)%2)//1

print ('%.d' %n01)
print ('%.d' %n02)
print ('%.d' %n03)
print ('%.d' %n04)
print ('%.d' %n05)
