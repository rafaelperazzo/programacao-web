# -*- coding: utf-8 -*-
import math
n= int(input('Digite o número de divisores desejados:'))
a= int(input('Digite o Primeiro número:'))
b= int(input('Digite o Segundo número:'))

i=1
while i<=n:
    a=a*i
    b=b*i
    i=i+1
    print(a)
    print(b)
  



