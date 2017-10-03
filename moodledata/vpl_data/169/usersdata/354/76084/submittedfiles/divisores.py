# -*- coding: utf-8 -*-
import math

n=int(input('digite o n: '))
a=int(input('digite o a (a>0): '))
b=int(input('digite o b (b>0): '))
#PROCESSAMENTO
multiploa:1
multiplob:1
while (n>=a) or (n>=b):
    multiploa=n/a
    multiplob=n/b
print(multiploa)
print(multiplob)
    
