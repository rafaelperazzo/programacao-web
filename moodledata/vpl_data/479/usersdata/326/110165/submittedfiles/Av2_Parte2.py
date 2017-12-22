# -*- coding: utf-8 -*-
import math
a = int(input('Digite a: '))
b = int(input('Digite b: '))

while a <= 0:
    a = int(input('Digite a: '))
while b <= 0:
    b = int(input('Digite b: '))
n=0
mdc=0
for i in range(2, n, 1):
    if a//n==0:
        a/n = mdc
    if b//n==0:
        b/n = mdc
        if a/n == b/n:
            print(mdc)
         
        
    
    
        
       