# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Insira o valor de n: '))
x = 1
y = n*(n-1)
while n > 0:
    x = x*y
    n = n-1
print(x)    