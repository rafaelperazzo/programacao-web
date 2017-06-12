# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma1=0
    for i in range (0,len(lista),1):
        soma1= soma1 +((lista[i]-media)**2)
    desvio=(soma1/(n-1))**(0.5)
    return desvio
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o numero de elementos da lista:'))
a=[]
b=[]
for i in range (1,n+1,1):
    numeroa=int(input('Digite o valor de um numero da lista a:'))
    a.append(numeroa)
for i in range(1,n+1,1):
    numerob=int(input('Digite o valor de um numero da lista b:'))
    b.append(numerob)
print(resultado(lista[a]))
print(desvio(lista[a]))
print(desvio(lista[b]))