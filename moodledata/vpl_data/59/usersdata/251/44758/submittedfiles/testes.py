# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite o número de termos: '))
valor = 0
soma = 0
for i in range(1,n+1,1):
    valor = float(input('Digite o valor do termo: '))
    soma = soma+valor
media = soma/n    
print(media)