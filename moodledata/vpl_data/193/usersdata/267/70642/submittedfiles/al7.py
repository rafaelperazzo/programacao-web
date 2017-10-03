# -*- coding: utf-8 -*-
n=int(input("Forneça um número: "))
soma=0
i=1
while (i<n):
    if n%i==0:
        print(i)
        soma=soma+i
    i=i+1
if(soma==n):
    print("PERFEITO")
else:
    print("NÃO PERFEITO")
