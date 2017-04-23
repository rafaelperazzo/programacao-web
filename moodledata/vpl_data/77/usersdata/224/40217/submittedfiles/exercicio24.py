# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
cont=0
i=1
for i in range(1,(n+1),1):
    if (a%i==0) and (b%i==0):
        cont=cont+i
print(cont)
