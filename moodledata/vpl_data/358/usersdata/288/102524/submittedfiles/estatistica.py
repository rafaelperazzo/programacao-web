# -*- coding: utf-8 -*-


def media(lista):
    media=sum(lista)/len(lista)
    return media

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio_padrao(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma+=((media(lista)-lista[i])**2)
    desvio=(soma/(n-1))**0.5
    return desvio
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.

m=int(input("Digite a quantidade de colunas: "))
n=int(input("Digite a quantidade de linhas: "))

matriz=[]
for i in range (0,m,1):
    linha=[]
    for j in range (0,n,1):
        linha.append(int(input("Digite o %d numero da  matriz: "%(j+1))))
    matriz.append(linha)
    
for i in range (0,m,1):
    print (media(matriz[i]))
    print ("%.2f"%(desvio_padrao(matriz[i])))