# -*- coding: utf-8 -*-
n=int(input('número de termos:'))
lista1=[]
lista2=[]

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
    
def desviopadrão(lista):
    soma2=0
    for i in range(0, len(lista), 1):
        soma2=soma2+(lista[i]-media(lista))**2
    desviopadrão=(soma2/(len(lista)-1))**0.5
    return (desviopadrão)
    
for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista1.append(numero)
    
for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista2.append(numero)
    
print('%.2f' %media(lista1))
print('%.2f' %desviopadrão(lista1))
print('%.2f' %media(lista2))
print('%.2f' %desviopadrão(lista2))
