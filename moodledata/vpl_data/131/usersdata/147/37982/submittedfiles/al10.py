# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
produto=0
n=1
termo=1
d=1
for termo in range(1,n+1,1):
    produto *== (n/d)*(n/(d+1))
    
print('%.5f'%produto)
    
    
        
    
