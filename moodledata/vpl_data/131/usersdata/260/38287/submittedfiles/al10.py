# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input("digite o número de termos desejado:"))
produto=1
for i in range (1,2*(n+1),2):
    produto=produto*((i+1)/(i))*((i+1)/(i+2))
    print(produto)
print(produto)