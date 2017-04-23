# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('numero de termos: '))
produto=1
num=1
den=2
termo=1
if n//2==0:
    while termo>=n: 
        produto=produto*(num/den)
        den=den+2
        num=num+2
print('%f'%produto)