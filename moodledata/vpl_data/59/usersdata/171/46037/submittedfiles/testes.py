# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
x=int(input('digite o valor de x:'))
expoente=1
den=1
i=0
for termo in range(1,n+1,1):
    valor=(x-(x**expoente))/(expoente*mathfactorial(den))
    if termo%2==1:
        i=i+valor
    else:
        i=i-valor
    expoente=expoente+2
    den=den+1
print(i)