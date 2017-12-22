# -*- coding: utf-8 -*-
import math
n= int(input('Quantos multiplos devem ser mostrados? '))
a= int(input('Digite o primeiro numero: '))
b= int(input('Digite o segundo numero: '))
teste= 1
c=0
while(c<n):
    if (teste%a)==0 or (teste%b)==0:
        print(teste)
        teste +=1
        c +=1
    else:
        teste +=1
