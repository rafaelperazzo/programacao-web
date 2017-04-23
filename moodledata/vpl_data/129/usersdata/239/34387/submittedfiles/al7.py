# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
i=1
contador=0
while i<(n):
    if n%i==0:
        contador=contador+i
        print(i)
    i=i+1
if contador>0:
    print("%d Perfeito"%n)
else:
    print("%d Não perfeito"%n)
    
