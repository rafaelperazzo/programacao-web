# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
menor=500
maior=0
for i in range(1,n+1,1):
    hf=int(input('digite h fem:'))
    hm=int(input('digite h masc:'))
    if hf>maior:
        maior=hf
    if hf<menor:
        menor=hf
print(maior)
print(menor)