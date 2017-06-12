# -*- coding: utf-8 -*-
n=int(input('Informe o número de termos:'))
lista1=[]
lista2=[]
def media(lista):
    soma1 = 0
    for i in range(0,len(lista),1):
        soma1= soma1+ lista[i]
    resultado = soma/len(lista)
    return resultado
def desvio_padrao(lista):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]/media))**2
    desvio_padrao=(soma2/(n-1))**(1/2)
    return (desvio_padrao)
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista1.append(numero)
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista2.append(numero)
print('%.2f' %media(lista1))

    
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 