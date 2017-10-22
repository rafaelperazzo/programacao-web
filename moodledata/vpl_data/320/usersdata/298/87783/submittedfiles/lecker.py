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
    
if lista[1]>lista[0] and lista[1]>lista[2]:
    soma=soma+1
if lista[h-2]>lista[h-3] and lista[h-2]>lista[h-1]:
    soma=soma+1

#os if resolveram tudo, acredito, mas coloquei a repetição para caso a lista tivesse mais que 4 elementos

for i in range (2, h-3, 1):
    if lista[i]>lista[i-1] or lista[i]>lista[i+1]:
        soma=soma+1
    if lista[i]==lista[i-1] and lista[i]==lista[i+1]:
        soma=soma+0

if soma==1:
    print('S')
if not soma==1:
    print('N')