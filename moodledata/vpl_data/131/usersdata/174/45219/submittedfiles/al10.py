# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Quantidade de termos:'))
for i in range(2,n+1,2):
    pi=(i/(i-1))*(i/(i+1))
print ('%.5f'%pi)