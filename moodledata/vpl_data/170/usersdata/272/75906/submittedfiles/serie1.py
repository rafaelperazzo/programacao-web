# -*- coding: utf-8 -*-
import math

n= int(input('Digite o valor de n: '))
num=1
den=1
contador=0
soma=0

while (contador<n):
    if (n%2==0):
        soma= soma - (num/den)
    elif (n%2==1):
        soma= soma + (num/den)
    
    num= num + 1
    den= num**2
    contador= contador + 1

print('%.5f' %soma)

    
