# -*- coding: utf-8 -*-
import math
num1= int(input('Digite um número: '))
num2= int(input('Digite outro número: '))

resto = None
while resto is not 0:
    resto = num1%num2
    num1=num2
    num2=resto
        
return num1
print(resto)
