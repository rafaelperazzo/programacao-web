# -*- coding: utf-8 -*-
n=int(input("Digite um número para verificação: "))
p=2
contador = 0
while p<(n-1):
    if n%p==0:
        contador = contador + 1
    p=p+1
if contador>0:
    print("%d não é primo"%n)
else:
    print("%d é primo"%n)