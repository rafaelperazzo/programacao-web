# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos da sequência'))
denominador=1
numerador=2
termo=1
produto=1
while termo<=n:
    produto=produto*(numerador/denominador)
    if numerador<denominador:
        numerador=numerador+2
    else:
        denominador=denominador+2
    termo=termo+1
resultado=produto*2
print('pi=%.5f'%resultado)
    