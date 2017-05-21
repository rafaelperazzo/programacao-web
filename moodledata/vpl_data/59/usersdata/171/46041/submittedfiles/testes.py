# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite o valor de n primeiros termos:'))
x=int(input('digite o valor de x:'))
expoente=1
den=1
i=0
for termo in range(1,n+1,1):
    valor=(x-(x**expoente))/(expoente*math.factorial(den))
    if termo%2==1:
        i=i+valor
    else:
        i=i-valor
    expoente=expoente+2
    den=den+1
print(i)