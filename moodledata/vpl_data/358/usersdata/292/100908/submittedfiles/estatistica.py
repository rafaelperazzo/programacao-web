# -*- coding: utf-8 -*-
from math import sqrt

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    
    def desv(resultado, lista):
        soma = 0
        for i in lista:
            soma += (i - resultado)**2
            
        desv_p = sqrt(soma/ (len(lista) - 1))
        
        return desv_p
        
    return (resultado, desv(resultado, lista))

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
m = int(input("Digite a quantidade de listas: "))
n = int(input("Digite a quantidade de elementos: "))

matriz = []
for i in range(1, m+1):
    linhas = []
    for j in range(1, n+1):
        linhas.append(float(input("Digite o %dº elemento da %dº lista: "%(j, i))))
        
    matriz.append(linhas)
    
for i in matriz:
    print("%.2f"%(media(i)[0]))
    print("%.2f"%(media(i)[1]))