# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvpadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    desv=(soma/(n-1))**0,5
    return desv

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('escreva o numero de elementos das listas:'))
a=[]
for i in range(0,n,1):
    valor=float(input('digite o numero a ser anexado a lista:'))
    a.append(valor)
b=[]    
for i in range(0,n,1):
    valor=float(input('digite o numero a ser anexado a lista:'))
    b.append(valor)
m=media(a)
print(%.2f%m)
dsv=desvpadrao(a)
print(dsv)
m=media(b)
print(m)
dsv=desvpadrao(b)
print(dsv)

    