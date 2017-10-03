# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
i = 2.0
j = 3.0
auxi = 2.0
auxj = 3.0
cont = 0

n = int(input())

while n>0:
    n = n - 1
    i = i * auxi
    auxi = auxi + 2
    if cont == 0:
        j = j * 1
        cont = cont + 1
    else:
        j = j * auxj
        auxj = auxj + 2
     
    

pi = i/j

print(pi)