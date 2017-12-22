# -*- coding: utf-8 -*-

lista=[]
n=int(input("Digite o valor de n: "))
soma=0
for i in range(0,n,1):
    num=int(input('digite o valor: '))
    lista.append(num)
    soma=soma+num
print('%.2f' %lista[0])

print('%.2f' %lista[len(lista)-1])


    

