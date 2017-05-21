# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos: '))
i=0
num=2
den=1
prod=1
while (i<=n):
    prod=prod*(num/den)
    if (i%2==1):
        num=num+2
    else:
        den=den+2
    i=i+1
print('%.5f' %prod)    