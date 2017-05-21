# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos: '))
pi=1
m=2
for i in range (1, n+1, 1):
    if (i<=n):
        r=(m/(m-1))*(m/(m+1))
        pi=pi*r
        m=m+2
    pi=pi*2
print('%.5f' %pi)    