# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input("digite o número de termos desejado:"))
produto=1
termo=1
for i in range (1,n+1,1):
    if i%2==0:
       produto=produto*(termo)/(termo+1) 
    else:
        produto=produto*(termo+1)/(termo)
    termo=termo+1
print(produto)