# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('digite o valor de n: '))
i=2
h=0
while (i<=n):
    pi=(i/(i-1))*h
    i=1+i
    h=i+1
    print(pi)
    