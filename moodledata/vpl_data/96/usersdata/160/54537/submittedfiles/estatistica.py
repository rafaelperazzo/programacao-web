# -*- coding: utf-8 -*-



def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma + ((lista[i]-media(lista)**2)
        resultado=(soma/len(lista))**2
    return(resultado)
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(0,n,1):
    valor1=int(input('Digite os elementos da lista 1:'))
    a.append(valor1)
b=[]
for i in range(0,n,1):
    valor2=int(input('Digite os elementos da lista 2:'))
    b.append(valor2)
    
print(media(a))
print(desvio(a))
print(media(b))
print(desvio(b))

