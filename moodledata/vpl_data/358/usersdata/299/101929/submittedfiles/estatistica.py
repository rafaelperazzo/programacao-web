# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desviopadrão(lista):
    soma1 = 0
    for i in range(0,len(lista),1):
        soma1 = soma1 + lista[i]
        x = soma1/len(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma+=(lista[i]-x)**2
    resultado = soma/(len(lista)-1)
    return resultado

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
for i in range(0,m,1):
    print(media(matriz[i]))
    print(desviopadrão(matriz[i]))
        


