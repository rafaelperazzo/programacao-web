# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Informe o número de termos:'))
numerador=2
denominador=1
pi=1
termo=1
while termo<=n:
    if numerador<denominador:
        pi=pi*(numerador/denominador)
        numerador=numerador+2
    elif numerador>denominador:
        pi=pi*(numerador/denominador)
        denominador=denominador+2
print('%.5f'%(pi*2))        