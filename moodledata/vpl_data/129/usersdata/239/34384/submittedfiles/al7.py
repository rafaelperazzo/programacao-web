# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
i=0
contador=0
while i<(n):
    if n%i==0:
        contador=contador+i
        print(i)
    i=i+1
if contador>0:
    print("%dPerfeito"%n)
else:
    print("%dNão perfeito"%n)
    
