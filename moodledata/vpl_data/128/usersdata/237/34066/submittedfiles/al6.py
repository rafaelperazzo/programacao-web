# -*- coding: utf-8 -*-
n=int(input("digite o numero: "))
i=2
while i<n:
    d=n%i
    if d==0:
        print(i)
    i=i+1
if n%i == 0:
    print("n é primo")


