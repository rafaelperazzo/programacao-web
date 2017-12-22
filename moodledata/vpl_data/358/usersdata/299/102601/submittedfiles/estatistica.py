# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio(lista):
    #media
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    x=soma/len(lista)
    
    #variancia
    var=[]
    for i in range(0,len(lista),1):
        var.append((x-lista[i])**2)
    variancia=(sum(var))/(len(lista)-1)
    #desvio
    desvio=(variancia)**(1/2)
    return desvio

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
matriz=[]
m=int(input(''))
n=int(input(''))
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        linha.append(float(input('')))
    matriz.append(linha)
for i in range(0,len(matriz),1):
    print('%.2f'%media(matriz[i]))
    print('%.2f'%desvio(matriz[i]))

