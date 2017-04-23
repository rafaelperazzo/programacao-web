# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos a ser calculado: '))
pi=1
i=2
for i in range (2,n+1,1):
    pi=pi*(i/(i-1))*(i/(i+1))
pi=pi*2
print('%.5f'%pi)
        
    