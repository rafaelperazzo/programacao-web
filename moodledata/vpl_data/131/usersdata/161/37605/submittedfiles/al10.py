# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Imforme o número de termos'))
numerador=1
denominador=2
produto=1
while termo<=n:
    produto=produto*(numerador/denominador)
    if numerador<denominador:
        produto=produto+2
    elif numerador>denominador:
        denominador=denominador+2
print('%.5f'(produto*2))        