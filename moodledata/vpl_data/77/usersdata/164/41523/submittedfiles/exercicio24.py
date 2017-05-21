# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
cont=0
for MDC in range (1,a+1,1):
    if (a%MDC==0) and (b%MDC==0):
        cont=cont+1
print(cont)