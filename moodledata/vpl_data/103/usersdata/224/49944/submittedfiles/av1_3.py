# -*- coding: utf-8 -*-
import math
p=int(input('Digite o primeiro valor: '))
q=int(input('Digite o segundo valor: '))
cont=0
if p>q:
    for i in range(1,p+1,1):
        cont=cont+1
else:
    for i in range(1,q+1):
        cont=cont+1
if p%i==0 and q%i==0:
    print(i)
print(cont)
