# -*- coding: utf-8 -*-
n=int(input("digite o numero: "))
i=2
while i<n:
    d=n%i
    if d==0:
        print(i)
    i=i+1
if d!= 0:
    print("n é primo")
else:
    print("n não é primo")
    

