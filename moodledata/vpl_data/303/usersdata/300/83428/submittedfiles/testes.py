# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Insira o valor de n: '))
x = 1
while n > 1:
    x*=n*(n-1)
    n-=1
print(x)    