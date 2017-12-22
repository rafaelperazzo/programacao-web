# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvioPadrao(lista):
    xbarra=media(lista)
    desvioQuadrado=0
    for i in range(0,len(lista),1):
        desvioQuadrado+=(xbarra-lista[i])**2
    nelementos=len(lista)-1
    desvio=(desvioQuadrado/nelementos)**0.5
    return desvio

def lelista:
    lista=[]
    tamanho=int(input('Digite o numero de elementos da lista: ' ))
    for i in range(tamanho):
        lista.append(int(input('Digite os elementos da lista: ')))
    return lista
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
quantaslistas=int(input('Digite quantas listas: '))
matriz=[]
for i in range(quantaslistas):
    matriz.append(lelistas())

for i in matriz:
    print('{:.2f}'.format(media(i)))
    print('{:.2f}'.format(desvioPadrao(i)))
        


