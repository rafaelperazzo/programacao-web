# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v=int(input('Digite seu saque: '))
q1=v//20
r1=v%20
q2=r1//10
r2=r1%10
q3=r2//5
r3=r2%5
q4=r3//2
r4=r3%2
q5=r4//1
r5=r4%1
print('{}\n{}\n{}\n{}\n{}'.format(q1,q2,q3,q4,q5))