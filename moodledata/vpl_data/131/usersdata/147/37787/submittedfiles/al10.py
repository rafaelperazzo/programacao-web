# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
produto=0
numerador=2
termo=1
denominador=1
for termo in range(1,n+1,1):
    produto=(numerador/denominador)*(numerador/(denominador+1))
    numerador=numerador+2
    denominador=denominador+2
print(produto)
    
    
        
    
