# -*- coding: utf-8 -*-
n=int(input('digite n:'))
lista1=[]
lista2=[]
def media(lista2):
    soma = 0
    for i in range(0,len(lista2),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desviopadrao(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+((lista[i]-media)**2)
    DP=(soma1/(n-1))**(0.5)
    return DP
for i in range(0,n,1):
    a=float(input('digite a:'))
    lista1.append(a)
for i in range(0,n,1):
    b=float(input('digite b:'))
    lista2.append(b)
print('%.2f' %resultado(lista1))
print('%.2f' %DP(lista1))
print('%.2f' %resultado(lista2))
print('%.2f' %DP(lista2))










#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 