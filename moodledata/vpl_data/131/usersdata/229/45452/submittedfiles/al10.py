# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA

n=int(input('digite a quantidade:'))
i=0
numerador=2
produto=1
denominador=1

while i <=n-1:
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador+2
    else:
        denomindor=denominador+2
    i=i+1
produto=produto*2
print('%.5f'%produto)