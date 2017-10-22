# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite o valor de n: '))
i = 1
cont = 0
while i<n:
    if i%2==1:
        cont = cont + i
    i = i + 1    
print(cont)