# -*- coding: utf-8 -*-
n=int(input('Digite n: '))
a=[]
b=[]
for z in range (1, n+1, 1):
    valorA=float(input('Valor da lista A: '))
    a.append(valorA)
def media(lista):
    soma=0
    for i in range(0, len(a) ,1):
        soma=soma+a[i]
    resultado=soma/len(a)
    return resultado
    
    

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 