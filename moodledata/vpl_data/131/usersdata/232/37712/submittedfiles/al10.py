# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('Digite o número de termos a ser calculado: '))
contador=1
i=2
for i in range (2,n+1,2):
    contador=contador*(i/(i-1))*(i/(i+1))
contador=contador*2
print('%.5f'%contador)
        
    