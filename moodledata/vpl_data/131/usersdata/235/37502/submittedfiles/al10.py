# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o numero de termos:'))
numerador=2
denominador=1
contagem=0
produto=0
while contagem<0:
    produto=produto*(numerador/denominador)
    if numerador<denominador:
        numerador=numerador+2
    else:
        denominador=denominador+2
resultado=produto*2
print('pi=%.5f' %resultado)