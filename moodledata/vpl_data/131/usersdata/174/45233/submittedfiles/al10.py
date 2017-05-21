# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Quantidade de termos:'))
pi=1
for i in range(2,n+1,2):
    pic=(i/(i-1))*(i/(i+1))
    pi=pi*pic
    pii=pi*pic
print ('%.5f' %pii)