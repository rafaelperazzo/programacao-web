# coding: utf-8 #
inicial = int(input('Volume inicial: '))
quantidade = int(input('Quantidade: '))
i = 1
while (i<=quantidade):
    z = input('Mudanca %d: ' % i)
    inicial += z
    i += 1
    if inicial>100:
        inicial = 100
    if inicial<0:
        inicial = 0
print(inicial)
    
 
 