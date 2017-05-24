# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import math
bin=int(input('Digite um número: '))
i=0
soma=0
while bin>0:
    m=bin%10
    soma=soma+m*2**i
    bin=bin//10
    i=i+1
print(soma)    

    



















