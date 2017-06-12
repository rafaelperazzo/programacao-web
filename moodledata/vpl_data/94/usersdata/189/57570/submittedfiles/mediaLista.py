# -*- coding: utf-8 -*-
n=int(input('digite o numero:'))
lista=[]
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado

for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista.append(numero)
    
print('%.2f' %lista[0])
print('%.2f' %lista[4])
print('%.2f' %media(lista))
print(lista)
        
        
        
    


