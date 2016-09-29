# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('n'))

n1=(n//20.0)
n2=(n%20)//10.0
n3=((n%20)%10)//5.0
n4=(((n%20)%10)%5)//2.0
n5=((((n%20)%10)%5)%2)//1.0

print('O valor de n1=%d:' %n1)
print('O valor de n2=%d:' %n2)
print('O valor de n3=%d:' %n3)
print('O valor de n4=%d:' %n4)
print('O valor de n5=%d:' %n5)