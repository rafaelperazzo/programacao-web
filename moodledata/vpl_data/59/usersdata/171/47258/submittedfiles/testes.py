# -*- coding: utf-8 -*-
import math
#COMECE AQUI ABAIXO
n=int(input('digite n:'))
menor=500
maior=0
soma=0
for i in range(1,n+1,1):
    hf=int(input('digite h fem:'))
    hm=int(input('digite h masc:'))
    if hf>maior:
        maior=hf
    if hf<menor:
        menor=hf
    if hm>maior:
        maior=hm
    if hm<menor:
        menor=hm
    soma=soma+hf
    media=(soma)/n
print(maior)
print(menor)
print(media)