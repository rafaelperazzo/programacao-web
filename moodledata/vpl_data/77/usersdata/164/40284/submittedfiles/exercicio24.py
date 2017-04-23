# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
for MDC in range (a,b+1,1):
    if (a%MDC==0):
        cont=cont+1
    if (b%MDC==0):
        cont=cont+1
if (MDC>=1):
    print(MDC)