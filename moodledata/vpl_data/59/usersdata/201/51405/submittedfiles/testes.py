# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
inicio=int(input('Digite inicio:'))
fim=int(input('Digite o fim:'))
x=1
while x<=10:
    if inicio<=x<=fim:
        print(inicio*x)
    x=x+1