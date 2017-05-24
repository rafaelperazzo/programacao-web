# -*- coding: utf-8 -*-
import math
a=int(input('Digite a:'))
b=int(input('Digite b:'))
ant=a
atual=b
resto=ant%atual
contador=1
while resto!=0:
    post=atual
    atual=resto
    resto=post%atual
    contador=contador+1
print("MDC(%d,%d)"% (atual,contador))