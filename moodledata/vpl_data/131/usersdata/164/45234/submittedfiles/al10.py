# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos: '))
pi=1
for i in range (2, n+1, 2):
    if (i<=n):
        r=(i/(i-1))*(i/(i+1))
        pi=pi*r
print('%.5f' %pi)    