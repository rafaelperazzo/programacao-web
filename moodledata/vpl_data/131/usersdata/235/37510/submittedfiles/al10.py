# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o numero de termos:'))
numerador=2
denominador=1
contagem=0
produto=1
while contagem<n:
    produto=produto*(numerador/denominador)
    if numerador<denominador:
        numerador=numerador+2
    else:
        denominador=denominador+2
    contagem=contagem+1
resultado=produto*2
print('pi=%.5f' %resultado)