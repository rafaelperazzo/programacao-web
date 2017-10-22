# -*- coding: utf-8 -*-
import math

#COMECE SEU CODIGO AQUI
T1=int(input('Qual o número de tomadas da primeira regua? '))
while T1 <=1:
    T1=int(input('Qual o número de tomadas da primeira regua? '))
T2=int(input('Qual o número de tomadas da segunda regua?  '))
while T2 <=1:
    T2=int(input('Qual o número de tomadas da segunda regua?  '))
T3=int(input('Qual o número de tomadas da terceira regua? '))
while T3 <=1:
    T3=int(input('Qual o número de tomadas da terceira regua? '))
T4=int(input('Qual o número de tomadas da quarta regua?   '))
while T4 <=1:
    T4=int(input('Qual o número de tomadas da quarta regua?   '))
notebooks=((T1+T2+T3+T4)-3)
print(notebooks)
    

