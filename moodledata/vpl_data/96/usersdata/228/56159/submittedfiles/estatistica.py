# -*- coding: utf-8 -*-
n=int(input('digite um numero de elementos seu arrombado:'))
lista1=[]
lista2=[]
for i in range(0,n,1):
    termo1=int(input('digite o número:'))
    lista1.append(termo1)
    
for i in range(0,n,1):
    termo2=int(input('digite o número:'))
    lista2.append(termo2)    

def media(a):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(a,resultado):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(((lista[i]-resultado)**2)/len(lista))
        return(soma)
print('%.2f'%media(lista1))
print('%.2f'%desviopadrao(lista1))
print('%.2f'%media(lista2))
print('%.2f'%desviopadrao(lista2))
        
        

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 






