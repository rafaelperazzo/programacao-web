# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n= int(input('Digite um inteiro de 0 a 13: '))
while n<0 or n>13:
    print('Número fora do intervalo')
    n= int(input('Digite um inteiro de 0 a 13: '))
    if 0<=n<=13:
        print(n)
        break
qua= n**2
print('O quadrado desse número é %d' %qua)
    