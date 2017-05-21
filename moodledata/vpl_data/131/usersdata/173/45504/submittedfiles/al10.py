# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
a=int(input('Digite a quantidade de termos: '))
i=0
n=2
d=1
p=1
while(i<a):
    p=p*(n/d)
    if(i%2==1):
        n=n+2
    else:
        d=d+2
    i=i+1
r=p*2
print('%.5f'%r)