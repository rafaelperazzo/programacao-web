# -*- coding: utf-8 -*-
import math

a = int(input('Digite um número: '))
maior=a
menor=a
for i in range(4):
    a=int(input('Digite um valor:'))
    if a>maior:
        maior=a
    elif a<menor:
        menor=a
print(menor)        
print(maior)