# -*- coding: utf-8 -*-
from __future__ import division
import math

v = int(input('valor a ser sacado '))

q20 = v//20
q10 = (v-(q20*20))//10
q5 = (v-(q20*20)-(q10*10))//5
q2 = (v-(q20*20)-(q10*10)-(q5*5)//2
q1 = (v-(q20*20)-(q10*10)-(q5*5)-(q2*2)

print(q20)