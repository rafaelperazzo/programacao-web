# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
i = 2.0
j = 3.0
auxi = 2.0
auxj = 3.0
cont = 0
cont1 = 0
cont2 = 1

n = int(input())

while n>0:
    n = n - 1
    
    if cont1 == 0:
        auxi = auxi + 2
        i = i * auxi
        cont1 = cont1 + 1
    else:
        i = i * auxi
        cont1 = cont1 - 1
    
    if cont2 == 0:
        auxj = auxj + 2
        j = j * auxj
        cont2 = cont2 + 1
    else:
        j = j * auxj
        cont2 = cont2 - 1
    
    if cont == 0:
        j = j * 1
        cont = cont + 1
        cont2 == 0
    

pi = i/j

print(pi)