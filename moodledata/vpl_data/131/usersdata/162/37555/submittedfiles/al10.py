# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite n:'))
soma=0
termo=1
numerador=1
denominador=n
while termo<=n:
    soma=soma+numerador/denominador
    termo=termo+1
    numerador=numerador+1
    denominador=denominador+1
    print('%.5f'%soma)