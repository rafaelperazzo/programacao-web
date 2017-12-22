# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma=0
    for r in range(0,len(lista),1):
        soma=soma+((a[r]-media(lista)**2)
    desvio= ((soma/(len(lista) -1))**0.5)
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('digite n: '))
a=[]
for j in range(0,n,1):
    x = int(input('digite: '))
    a.append(x)
b=[]    
for k in range(0,n,1):
    p= int(input('digite: '))
    b.append(p)
print(media(a))  
print(desvio(a))
print(media(b))
print(desvio(b))