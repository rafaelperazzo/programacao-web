# coding: utf-8 #
inicial = int(input('Volume inicial: '))
quantidade = int(input('Quantidade: '))
i = 1
while (i<=quantidade):
    z = input('Mudanca %d: ' % i)
    inicial -= z
    i += 1
print(inicial)
    
 
 