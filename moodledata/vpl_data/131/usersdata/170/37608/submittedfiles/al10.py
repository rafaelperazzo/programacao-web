# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite a quantidade de termos:'))
if n<0:
    n=(-1)*n
soma=0
termo=1
numerador=1
denominador=n
while termo<=n:
    soma=soma+numerador/denominador
    termo=termo+1
    numerador=numerador+1
    denominador=denominador-1
print('%.5f'%soma)