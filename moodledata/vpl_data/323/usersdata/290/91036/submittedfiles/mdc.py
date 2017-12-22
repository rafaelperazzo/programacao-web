# -*- coding: utf-8 -*-
import math
a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
p=0
for i in range(1,a,1):
    if a%p==0 and b%p==0:
        p=i
print(p)
        
        


