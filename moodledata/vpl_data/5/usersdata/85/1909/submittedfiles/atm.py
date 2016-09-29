# -*- coding: utf-8 -*-
from __future__ import division
import math

n= int(input('Digite um valor para n: ')

q1= n//20
q2= (n%20)//10
q3= ((n%20)%10)//5
q4= (((n%20)%10)%5)//2
q5= ((((n%20)%10)%5)%2)//1

print q1
print q2
print q3
print q4
print q5