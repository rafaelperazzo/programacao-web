# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
q=int(input('digite  a quantidade:'))

numerador=2
denominador=1
produto=1

while i<=q-1:
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denominador=denominador+2
    i=i+1
print('%.5f'%produto*2)    