# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Insira o valor de n: '))
x = 0
y = n-1
while n > 1:
    x = x*n*y
    n = n-1
print(x)    