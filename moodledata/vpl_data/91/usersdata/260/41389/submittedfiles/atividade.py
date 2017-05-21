# -*- coding: utf-8 -*-
n = int(input("digite o número"))
contador=0
if n == 0:
    print(1)
else: 
while (n > 0):
    n=n//10
    contador=contador+1
print(contador)
