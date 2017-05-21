# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
if a>b:
    menor=b
else:
    menor=a
while a!=0 and b!=0:
    if a%b==0:
        mdc=a//b
print(mdc)    
    
    
