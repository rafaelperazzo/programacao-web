# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Informe o número de termos:'))
numerador=2
denominador=1
pi=1
for termo in range(1,n+1,1):
    pi=pi*(numerador/denominador)
    if numerador<denominador:
        pi=pi+2
    elif numerador>denominador:
        denominador=denominador+2
print('%.5f'%(pi*2))        