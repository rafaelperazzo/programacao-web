# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
list1=[]
n1=int(input('Digite a quantidade de termos: '))
soma1=0

for i in range (0,n,1):
    numero1=int(input('Digite o numero: '))
    list1.append(numero)
    soma11=soma1+numero

media1=soma1/n
somatorio1=0

for l in range(0,n,1):
    somatorio1=somatorio1+((list1(l)-media1))**2

desvio=((1)/(n-1)*(somatorio)**0.5

print
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 