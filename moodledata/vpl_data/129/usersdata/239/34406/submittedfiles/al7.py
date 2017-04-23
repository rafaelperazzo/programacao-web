# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
i=1
contador=0
while i<(n-1):
    if n%i==0:
        contador=contador+i
        print(i)
    i=i+1
if contador==n:
    print("%d Perfeito")
else:
    print("%dNão perfeito")
    
