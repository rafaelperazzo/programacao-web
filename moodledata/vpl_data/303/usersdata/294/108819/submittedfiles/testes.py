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
rai= n**(0.5)
sucessor= n+1
antecessor= n-1
print('O quadrado desse número é %d' %qua)
print('A raiz desse número é %.2f' %rai)
print('O sucessor desse número é %d' %sucessor)
print('O antecessor desse número é %d' %antecessor)