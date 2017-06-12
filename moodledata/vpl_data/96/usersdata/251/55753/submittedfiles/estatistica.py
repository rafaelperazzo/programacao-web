# -*- coding: utf-8 -*-
def desvPad (lista,media):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i]-media)**2)
        
    variancia=soma/(len(lista)-1)
    desvioPadrao=variancia**(0.5)
    return(desvioPadrao)
    
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

lista1 = [] 
lista2 = []
n = int(input('Digite a quantidade de termos da lista: '))

for i in range(0,n,1):
    termo=int(input('Digite o valor do termo '+str(i)+' da lista 1: '))
    lista1.append(termo)
    
for i in range(0,n,1):
    termo=int(input('Digite o valor do termo '+str(i)+' da lista 2: '))
    lista2.append(termo)    

print(media(lista1))
print('%.2f'%desvPad(lista1,media(lista1)))

print(media(lista2))
print('%.2f'%desvPad(lista2,media(lista2)))

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 