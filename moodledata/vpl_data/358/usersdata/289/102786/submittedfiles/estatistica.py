# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvioPadrao(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma+=((lista[i]-(media(lista))))**2
    var=soma/((len(lista))-1)
    desvio=(var)**(0,5)
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.
m=int(input("Digite a quantidade de listas: "))
n=int(input("Digite a quantidade de elementos de cada lista: "))
matriz=[]
for i in range(0,m,1):
    lista=[]
    for j in range (0,m,1):
        lista.append(int(input("Digite o elemento%.d da lista: " %(j+i))))
    matriz.append(lista)
for i in range(0,m,1):
    print(media(matriz[i]))
    print('%.2f' %(desvioPadrao(matriz[i])))