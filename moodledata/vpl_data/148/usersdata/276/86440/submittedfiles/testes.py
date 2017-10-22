# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
pa = float(input('Digite o valor de pa: '))
pb = float(input('Digite o valor de pb: '))
pc = float(input('Digite o valor de pc: '))

media_ponderada = ((a*pa) + (b*pb) + (c*pc))/(pa+pb+pc)

print (media_ponderada)