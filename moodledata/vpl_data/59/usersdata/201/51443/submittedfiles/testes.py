# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=float(input('Depósito inicial:'))
t=float(input('Taxa de juros:'))
for i in range(1,25,1):
    total=n+(n*t)
    print(total)
    n=total
    