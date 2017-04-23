# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('numero de termos: '))
produto=1
num=2
den=1
termo=1
for i in range(1,n,2):
    produto=produto*(num/den)
    den=den+2
    num=num+2
print('%f'%produto)