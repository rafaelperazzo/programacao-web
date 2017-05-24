# -*- coding: utf-8 -*-
import math
a=int(input('digite a:'))
b=int(input('digite b:'))
cont=0
i=1
for i in range(1,b+1,1):
    if a>b:
        a%i==0
        cont=cont+1
        i=i+1
if cont==0:
    print(MDC)
else:
    print('Nao existe')

        

