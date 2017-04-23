# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('numero de termos: '))
produto=1
num=2
den=1
termo=1
while termo<=n:
    produto=produto*(num/den)
    num=num+2
    den=den+2
    termo=termo+2
print('%f'%produto)