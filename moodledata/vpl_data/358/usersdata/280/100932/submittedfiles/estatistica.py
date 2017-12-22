# -*- coding: utf-8 -*-
import numpy as np

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvpad(a,n):
    med=sum(a)/len(a)
    somat=0
    for i in range(0,len(a),1):
        somat=somat + ((a[i]-med)**2)
    desvpad=(((1/n-1)*(somat))**0.5)
    return desvpad
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m=int(input("Digite m: "))
n=int(input("Digite n: "))
matriz=np.empty([m,n])

for i in range(0,m,1):
    for j in range(0,n,1):
        matriz[i][j]=int(input("Digite um valor: "))

for i in range(0,m,1):
    print(media(matriz[i]))
    print(desvpad(matriz[i]))


