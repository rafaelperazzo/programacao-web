# -*- coding: utf-8 -*-
import math
n=int(input('Digite n: '))
cont=0
soma=0
b=n
i=1
while i<b:
   c=b//10
   cont=cont+1
   i=i+1
   b=b%10
d=cont
while n>0:
    soma=soma+2*(n%10**(d-1))
    d=d-1
print(soma)