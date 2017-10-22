# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI


x= int(input('Digite a quantidade de números para tomada 1: '))
while (x<1):
    print('Número inválido, por favor digite um valor válido')
    x= int(input('Digite a quantidade de números para tomada 1: '))
y= int(input('Digite a quantidade de números para tomada 2: '))
while (x<1):
    print('Número inválido, por favor digite um valor válido')
    y= int(input('Digite a quantidade de números para tomada 2: ')) 
z= int(input('Digite a quantidade de números para tomada 3: '))
while (x<1):
    print('Número inválido, por favor digite um valor válido')
    z= int(input('Digite a quantidade de números para tomada 3: '))
t= int(input('Digite a quantidade de números para tomada 4: '))
while (x<1):
    print('Número inválido, por favor digite um valor válido')
    t= int(input('Digite a quantidade de números para tomada 4: '))

TOTAL= (x-1)+y+z+t
print (TOTAL)
