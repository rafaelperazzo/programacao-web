# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite n:'))
produto=1
i=2
for i in range (1,n+1,2):
    produto=produto*(i/(i-1))*(i/(i+1))
print(produto)    
