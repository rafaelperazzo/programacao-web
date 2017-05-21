# -*- coding: utf-8 -*-
a=int(input('Digite o valor a: '))
b=int(input('Digite o valor b: '))
cont=0
for i in range(1,a+b,1):
    if (a%i==0) and (b%i==0):
      cont=i
print(cont)

    