# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
b=0
a=100
for i in range(0,a,1):
    if a%(i+1)!=0:
        b = b + 1
print (b)

#...
#a = int(input('Digite o valor inicial: '))
#b = float(input('Digite o valor do juros anual: '))
#for i in range (a,a+10,1):
#    a = a + a*b
#    print('%.2f' %a)
#...