# -*- coding: utf-8 -*-
n=int(input("Digite um número para verificação: "))
p=2
contador = 0
while p<(n-1):
    if n%p==0:
        contador=contador+1
    p=p+1
if contador>0:
    if n%3==0 or n%5==0:
        print(3)
        print(5)
    print("%d NÃO PRIMO"%n)
   
else:
    print("%d PRIMO"%n)