# -*- coding: utf-8 -*-
import math

n= int(input('Digite a quantidade de múltiplos a serem mostrados: '))
a= int(input('Digite um valor para o intervalo: '))
b= int(input('Digite outro valor para o intervalo: '))

mult= 1
k=0

while k<n:
    if mult%a==0 or mult%b==0:
        print(mult)
        k += 1
    mult += 1
    

  
        