# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Imforme o número de termos:'))
numerador=1
denominador=2
termo=1
pi=1
while termo<=n:
    pi=pi*(numerador/denominador)
    if numerador<denominador:
        pi=pi+2
    elif numerador>denominador:
        denominador=denominador+2
print('%.5f'(pi*2))        