# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
numerador = 2
denominador = 1

n = int(input('Digite n: '))
pi = 1
for i in range(1,n+1,1):
    if i%2==1: #TERMO IMPAR
        pi = pi*(numerador/denominador)
        denominador = denominador + 2
    else:
        pi = pi*(numerador/denominador)
        numerador = numerador + 2

pi = pi * 2
print (pi)