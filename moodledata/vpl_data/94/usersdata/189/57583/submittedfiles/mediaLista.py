# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite o numero:'))
for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista.append(numero)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
    media=soma/len(lista)
    
print('%.2f' %lista[0])
print('%.2f' %lista[n-1])
print('%.2f' %media)
print(lista)
        
        
        
    


