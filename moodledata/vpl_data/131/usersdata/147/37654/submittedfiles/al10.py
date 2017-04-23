# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
produto=0
termo=1
denominador=1
for termo in range(2,n+1,2):
    termo=termo+1
    produto=((produto+2)/denominador+1)
print(produto)
    
    
        
    
