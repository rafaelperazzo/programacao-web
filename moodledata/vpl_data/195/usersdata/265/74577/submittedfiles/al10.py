# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n = int(input('digite o valor de n: '))
i=2
while (i<=n):
    pi=(i/(i-1))
    i=1+i
    contador=pi*i
    print(contador)
    