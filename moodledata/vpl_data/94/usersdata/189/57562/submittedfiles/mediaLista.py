# -*- coding: utf-8 -*-
n=int(input('digite o numero:'))
lista=[]
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
def desviopadrao(lista):
    soma1=0
    for i in range(0, len(lista),1):
        soma1=soma1+(lista[i]-media(lista))**2
    desviopadrao=(soma1/(len(lista)-1))**0.5
    return (desviopadrao)
    
for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista.append(numero)
print(lista[0])
print(lista[4])
print('%2.f' %media(lista))
print('%2.f' %desviopadrao(lista))
        
        
        
    


