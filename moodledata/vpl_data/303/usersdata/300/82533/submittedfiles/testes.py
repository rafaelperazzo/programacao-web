# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
i = 1
n = int(input('Digite o valor de n:' ))
while n <= 0:
    n = int(input('Digite o valor de n:' ))
while i <= n:
    print(i**2)
    i = i+2
    