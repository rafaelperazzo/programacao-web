# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=float(input('digite o numero de termos:'))

numerador=2 
denominador=1
i=0
produto=1
while i<=n:

    produto=produto*denominador/numerador
    if (i%2==1):
        numerador=numerador+2
    else:
        denominador=denominador+2       
    i=i+1