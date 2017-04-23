# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos a ser calculado: '))
i=2
pi=1
for i in range (1,n+1,1):
    pi=pi*(i/(i-1))*(i/(i+1))
pi=pi*2
print('%.5f'%pi)
        
    