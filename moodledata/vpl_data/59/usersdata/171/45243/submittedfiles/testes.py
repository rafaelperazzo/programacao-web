# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
k=int(input('digite o valor de k:'))
n=k
pi=0
soma=0
den=1
for termo in range(0,n+1,1):
    if termo%2==0:
        valor=4/den
        soma=soma+valor
    else:
        valor=4/den
        soma=soma-valor
    den=den+2
pi=pi+soma+(-1**k)*4/((2*k)+1)
print('%.6f'%pi)

   