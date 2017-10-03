# -*- coding: utf-8 -*-
import math
num1=int(input('Digite n1: '))
num2=int(input('Digite n2: '))

def mdc(num1,num2):
    resto=1
    while resto is not 0:
        resto=num1%num2
        num1=num2
        num2=resto
        
    return num1
    
print (mdc)
