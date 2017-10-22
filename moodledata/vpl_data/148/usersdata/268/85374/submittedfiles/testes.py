# -*- coding: utf-8 -*-
n=int(input('Digite o valor a ser sacado : '))
v=20
while(n>0):
    quantidade= n//v
    print(quantidade)
    n= n - (n//v)*v
    v=v//2
  