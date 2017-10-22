# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('digite o valor de um número inteiro não-negativo: '))
i = 1
cont = 1
while i<=n:
    if n>0:
        cont = cont*i
        i = i + 1
print('%d! = %d' % (n,cont))        