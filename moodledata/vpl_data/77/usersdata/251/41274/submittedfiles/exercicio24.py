# -*- coding: utf-8 -*-
import math
a = int(input('Digite um valor qualquer para a: '))
b = int(input('Digite um valor qualquer para b: '))
divisor = 0
if a<b:
    for i in range(1,a+1,1):
        if a%i==0 and b%i==0:
            divisor = i
    print(divisor)
    
else:
    for i in range(1,a+1,1):
        if b%i==0 and a%i==0:
            divisor = i
    print(divisor)
