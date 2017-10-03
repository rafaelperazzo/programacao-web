# -*- coding: utf-8 -*-
#NÃO APAGUE A LINHA ACIMA. COMECE ABAIXO DESTA LINHA
i = 2.0
j = 3.0
cont = 0

n = int(input())
while n!=0:
    n = n - 1
    i = i * i
    if cont == 0:
        j = j * 1
        cont = cont + 1
    else:
        j = j * j
     
    

pi = i/j
print('%.2f' %pi)