# -*- coding: utf-8 -*-
n = int(input("Valor de n: "))
i=1
s=0
while (i<n):
    if (n%i)==0:
        s=s+i
        print(i)
    i=i+1
if s==n:
    print("PERFEITO")
else:
    print("NÃO PERFEITO")