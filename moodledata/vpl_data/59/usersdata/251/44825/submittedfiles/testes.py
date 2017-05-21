# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite o número de termos: '))
valor = 0
soma = 0
somaQuadrada
for i in range(1,n+1,1):
    valor = float(input('Digite o valor do termo '+str(i)+': '))
    soma = soma+valor
    somaQuadrada=somaQuadrada+(valor**2)
media = soma/n    
desvio=((somaQuadrada/n)-(media**2))**0.5
print('A média é: %.3f'%media)
print('O desvio é: %.5f'%desvio)
