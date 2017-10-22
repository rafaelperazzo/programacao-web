# -*- coding: utf-8 -*-
import math
a = int(input('Digite o primeiro número da sequência: '))
b = int(input('Digite o segundo número da sequência: '))
c = int(input('Digite o terceiro número da sequência: '))
d = int(input('Digite o quarto número da sequência: '))

lista=[a, b, c, d]
soma=0
h=len(lista)

if lista[0]>lista[1]:
    soma=soma+1
if lista[0]==lista[1]:
    soma=soma+0
    
if lista[h-2]<lista[h-1]:
    soma=soma+1
if lista[h-2]==lista[h-1]:
    soma=soma+0
    
for i in range (0, h-1, 1):
    if lista[i]>lista[i-1] or lista[i]>lista[i+1]:
        soma=soma+1
    if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
        soma=soma+0

if soma==1:
    print('S')
if not soma==1:
    print('N')