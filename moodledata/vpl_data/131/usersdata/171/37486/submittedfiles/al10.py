# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
pi=3.00217
termo=2
numerador=2
denominador=1
while termo<=n:
    if termo%2==0:
        soma=soma+2/denominador
        termo=termo+2
        denominador=denominador+2
print(soma)