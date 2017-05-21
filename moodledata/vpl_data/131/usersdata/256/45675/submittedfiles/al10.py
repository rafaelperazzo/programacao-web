# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número:' ))
i=o
numerador=2
denominador=1
produto=1
while i <=(n-1):
    produto=produto*numerador/denominador
    if i%2==1:
        numerador=numerador=2
    else:
        denominador=denominador=2
    i=i+1
print(%.5f%*produto)