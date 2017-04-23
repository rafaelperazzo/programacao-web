# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
i=1
contador=0
while i<n :
    d=n%i
    if d==0:
        contador=contador+i
        print(i)
    i=i+1
if contador==n:
    print("PERFEITO")
elif contadro!=n:
    print("NÃO PERFEITO")
