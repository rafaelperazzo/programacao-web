# -*- coding: utf-8 -*-
n= int (input('Digite a quantidade de elementos: '))
a=[]

for i in range (0,n,1):
    valor_a = int(input('Digite o elemento da lista:' ))
    a.append (valor_a)

print ('%.2f' %a[0])
print ('%.2f' %a[n-1])

def media (lista):
    soma = 0
    for i in range (0,len(lista),1): 
        soma = soma + a[i]
        
    media = soma/n
    return (media)

print ('%.2f' %media (a))
print (a)
