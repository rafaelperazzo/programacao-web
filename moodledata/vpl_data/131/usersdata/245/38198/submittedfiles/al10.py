# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite o valor de n:'))
n1=2
d1=1
p=1
termo=1
while termo<= n:
    if n1>d1:
        p=p*(n1/d1)
        d1=d1+2
    elif d1>n1:
        p=p*(n1/d1)
        n1=n1+2
x=p*2
print('%.5f'%x)
