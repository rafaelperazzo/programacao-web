# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('digite o valor de n: '))
i=2
pi=1
while (i<=n):
    m=pi*(i/(i-1))
    pi=i
    i=1+i
    print(m)
    