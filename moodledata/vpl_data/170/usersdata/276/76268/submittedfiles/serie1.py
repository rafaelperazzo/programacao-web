# -*- coding: utf-8 -*-
import math
n = int(input('Digite o valor de n: '))

posicao = 1
soma = 0

while (posicao<=n):
    if (posicao%2!=0):
        numerador1 = posicao
        denominador1 = (posicao**2)
        fracao1 = (numerador1/denominador1)
        soma = soma + fracao1
        
    elif (posicao%2==0):    
        numerador2 = posicao
        denominador2 = (posicao**2)
        fracao2 = (numerador2/denominador2)
        soma = soma - fracao2
    
    posicao = posicao+1

print (soma)