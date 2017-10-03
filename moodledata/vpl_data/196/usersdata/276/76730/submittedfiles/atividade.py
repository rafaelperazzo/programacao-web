# -*- coding: utf-8 -*-
import math

n = int(input('Digite o valor de n: '))

contador = 1
soma = 0
i = 0

while (contador<=n):
    numerador = contador
    denominador = n-i
    soma = soma + (numerador/denominador)
    
    if (n<0):
        n = -n
        numerador = contador
        denominador = n-i
        soma = soma + (numerador/denominador)
    
    i = i+1
    contador = contador + 1
    
print ('%.5f' %soma)
    