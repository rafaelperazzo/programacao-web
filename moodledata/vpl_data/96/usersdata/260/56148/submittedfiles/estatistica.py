# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista,n,media):
    s1=0
    s=0
    for i in range(0,len(lista),1):
        s1=s1+(lista[i]-media)**2
    s=1/(n-1)*s1
    s=s**(1/2)
    return s
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
lista=[]
n=int(input("digite a quantidade de elementos"))
for i in range(0,n,1):
    lista.append(int(input("digite o valor do elemento")))
desvio=s
media=resultado
print("%.2f %media)
print("%.2f %media)