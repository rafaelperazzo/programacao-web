# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma+(lista[i]-media(lista))
    desvio = ((soma)**(1/2))/len(lista)
    return desvio
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de coluna: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(float(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)
#media
print(media(matriz[0]))


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 