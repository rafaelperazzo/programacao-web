# -*- coding: utf-8 -*-
import math
#ENTRADA
n = int(input('Digite o valor de n : '))
soma = 0
num = 1
den = (num**2)
#PROCESSAMENTO
while (num<=n) :
    if(num%2==0) :
        soma = soma-(num/den)
    else :
        soma = soma+(num/den)
    num = num+1
print(soma)
        
