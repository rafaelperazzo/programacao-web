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
        soma = soma + (lista[i]-media(lista))**2
    desvio = (soma/(len(lista)-1))**(1/2)
    return desvio
m = int(input('Digite a quantidade de linhas: '))
n = int(input('Digite a quantidade de coluna: '))
matriz = []
for i in range(m):
    linha = []
    for j in range(n):
        linha.append(float(input('Digite o elemento %d de %d: '%((j+1),(i+1)))))
    matriz.append(linha)
#media
for i in range(m):
    print('%.2f'%(media(matriz[i])))
    print('%.2f'%(desviopadrao(matriz[i])))


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 