# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite um valor n:'))
i=2
contador=0
while i<=(n):
    soma=((i/(i-1))*(i/(i+1)))*2
    contador=contador+1
    i=i+1
print('%.5f'%soma)    

    
    
