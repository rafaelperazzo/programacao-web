# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('numero de termos: '))
produto=1
num=2
den=1
termo=1
while termo//2==0: 
    produto=produto*(num/den)
    den=den+2
    num=num+2
    tormo=termo+1
print('%f'%produto)