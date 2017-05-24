# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import math
bin=int(input('Digite um texto: '))
i=0
soma=0
while bin>0:
    m=n%10
    soma=soma+m*2**i
    n=n//10
    i=i+1
print(soma)    
    



















