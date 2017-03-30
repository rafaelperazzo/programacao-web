# -*- coding: utf-8 -*-
c=floatinput('Digite o nome de um polígono convexo de 3 a 6 lados:'))
triângulo=3
quadrilátero=4
pentágono=5
hexágono=6
c=float(input('Digite o nome de um polígono convexo de 3 a 6 lados:'))
nd=c*(c-3)/2
print('O número de diagonais do polígono é:%1f'%nd)