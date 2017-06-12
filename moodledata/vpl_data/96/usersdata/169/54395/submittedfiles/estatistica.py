# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Elementos:'))
l1=[]
l2=[]
def media(lista):
    sm=0
    for i in range(0,len(lista),1):
        sm=soma+lista[i]
    resultado=sm/len(lista)
    return resultado
    
def dsvpadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2 
    dsvpadrao=(soma/(len(lista)-1))**(0.5)
    return dsvpadrao
for i in range(0,n,1):
    n1=float(input('Digite o Elemento da Lista:'))
    l1.append(numero)
for i in range(0,n,1):
    n1=float(input('Digite o Elemento da Lista:'))
    l2.append(numero)
print('%.2f' %media(l1))
print('%.2f' %dsvpadrao(l1))
print('%.2f' %media(l2))
print('%.2f' %dsvpadrao(l2))





#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 