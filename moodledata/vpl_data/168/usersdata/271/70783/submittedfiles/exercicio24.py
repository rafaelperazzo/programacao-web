# -*- coding: utf-8 -*-
import math
#ENTRADA
x = int(input('Digite o valor de x : '))
y = int(input('Digite o valor de y : '))
i = 1
mdc = 1
#PROCESSAMENTO
if (x>y) :
    while(i<=y) :
        if (x%i)== 0 and (y%i)== 0 :
            mdc = i
        i=i+1
if (x<y) :
    while(i<=x) :
        if(x%i)== 0 and (y%i)== 0 :
            mdc = i
        i=i+1
#SAIDA
print(mdc)
        



