# -*- coding: utf-8 -*-
import math

n=int(input('digite o n: '))
a=int(input('digite o a (a>0): '))
b=int(input('digite o b (b>0): '))
#PROCESSAMENTO
multiplo:0
while (n>=a) or (n>=b):
    n=n/a
    n=n/b
    multiplo=multiplo+1
print(multiplo)
    
