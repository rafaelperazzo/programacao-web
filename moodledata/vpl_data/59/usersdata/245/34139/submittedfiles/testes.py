# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um número inteiro:'))
factorial=n
for i in range(1,n,1):
    factorial=factorial*i
print(factorial)