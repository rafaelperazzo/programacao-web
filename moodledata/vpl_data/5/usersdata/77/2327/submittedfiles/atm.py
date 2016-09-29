# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input(''))

n1=(n//20.0)
n2=(n%20)//10.0
n3=((n%20)%10.0)//5.0
n4=(((n%20)%10.0)%5.0)//2.0
n5=((((n%20)%10.0)%5.0)%2.0)//1.0

print('%d'%n1)
print('%d'%n2)
print('%d'%n3)
print('%d'%n4)
print('%d'%n5)