# -*- coding: utf-8 -*-
n = int(input("Valor de n: "))
i=2
soma=0
while (i<n):
    if(n%i)==0:
        soma=soma+1
        print(i)
    i=i+1
if soma==0:
    print("PRIMO")
if soma>0:
    print("NÃO PRIMO")