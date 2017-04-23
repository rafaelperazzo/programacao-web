# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Informe o número de termos: '))
pi=1
numerador=1
denominador=2

for n in range(1,n+1,1):
    if numerador > denominador:
        pi = pi*(numerador/denominador)
        denominador = denominador + 2
    elif numerador < denominador:
        pi=pi*(numerador/denominador)
        numerador=numerador+2
print('%5.f'%(pi*2))