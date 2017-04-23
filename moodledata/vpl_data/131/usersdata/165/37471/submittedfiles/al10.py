# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input('digite um valor para n:'))
pi=0
i=2
for i in range (2,n+1,1):
    pi=pi+i/(i-1)*i/(i+1)
    i=i+2
print(pi)    
