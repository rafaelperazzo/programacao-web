# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
while (x%y)!=0:
    x=y
    y=(x%y)
    resto=(x%y)
    print (resto)