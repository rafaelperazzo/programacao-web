# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma =float( soma + lista[i])
    resultado = float(soma/len(lista))
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvpad(lista):
    somatorio=0
    media=sum(lista)/n
    for j in range(0,n,1):
        somatorio=somatorio+((lista[i]-media)**2)
    resultado=((1/(n-1))*somatorio)**(0.5)
    return resultado
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.
matriz=[]
m=int(input('digite o número de listas: '))
n=int(input('digite o número de elementos: '))
for i in range(0,m,1):
    lista=[]
    for j in range(0,n,1):
        lista.append(float(input('digite o valor da lista%d e posição%d : '%((i+1),(j+1)))))
    matriz.append(lista)
for i in range(0,m,1):
    print('%.2f'%media(matriz[i]))
    print('%.2f'%desvpad(matriz[i]))