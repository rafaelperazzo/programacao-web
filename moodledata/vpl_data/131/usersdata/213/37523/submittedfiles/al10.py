# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Informe o número de termos: ')

pi=1
numerador=1
denominador=2

for termo in range(1,n+1,1):
    if numerador > denominador:
        pi = pi*(numerador/denominador)
        