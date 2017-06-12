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
    for i in range (0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
        
    soma=(soma/(len(lista)-1))**(0.5)
    return soma
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o numero de elementos da lista:'))
a=[]
b=[]
for i in range (0,n,1):
    numero=int(input('Digite o valor de um numero da lista a:'))
    a.append(numero)
for i in range(0,n,1):
    numero=int(input('Digite o valor de um numero da lista b:'))
    b.append(numero)
mediaA=media(a)
print('%.2f'%mediaA)
desvioA=desvio(a)
print('%.2f'%desvioA)
mediaB=media(b)
print('%.2f'%mediaB)
desvioB=desvio(b)
print('%.2f'%desvioB)