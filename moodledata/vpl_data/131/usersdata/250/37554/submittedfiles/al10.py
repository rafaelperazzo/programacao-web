# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite um valor n:'))
i=2
d=2
while n>0:
    soma=2*((i/(i-1))*(i/(i+1)))
    i=i+2
    d=d+2
    n=n-1
print('%.5f'%soma)    

    
    
