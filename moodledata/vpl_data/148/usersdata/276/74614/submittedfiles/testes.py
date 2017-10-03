# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int (input('Digite o valor de n: '))
numerador = 2
denominador = 1
pi2 = 1
contador = 1

while (contador<=n):
    primeira = numerador/(numerador-1)
    segunda = numerador/(numerador+1)
    pi2 = pi2*primeira*segunda
    numerador = numerador + 2
    contador = contador + 1

pi = pi2*2
print (pi)