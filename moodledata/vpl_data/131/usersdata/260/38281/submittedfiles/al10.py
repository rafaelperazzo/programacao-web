# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
n=int(input("digite o número de termos desejado:"))
produto=1
a=0
for i in range (1,n+1,1):
    produto=produto*((a+1)/(a))*((a+1)/(a+2))
    a=a+2
print(produto)