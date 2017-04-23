# -*- coding: utf-8 -*-
n=int(input("digite o numero: "))
i=2
contador=0
while i<n:
    d=n%i
    if d==0:
        contador=contador+1
        print(i)
    i=i+1
if contador==0 :
    print("PRIMO")
if contador!=0 :
    print("NÃO PRIMO")


