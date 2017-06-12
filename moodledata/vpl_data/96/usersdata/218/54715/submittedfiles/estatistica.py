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
        
    soma=(soma/(len(lista)-1))**(0,5)
    return soma


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas.
n=int(input('digite o numero de elementos da lista:'))
a=[]
b=[]
for i in range (0,n,1):
    elemento=int(input('digite o elemento a ser anexado a lista:'))
    a.append(elemento)
for i in range (0,n,1):
    elemento=int(input('digite o elemento a ser anexado a segunda lista:'))
    b.append(elemento) 

mediaa=media(a)
print('%.2f'%mediaa)

desvioa=desvio(a)
print('%.2f'%desvioa)

mediab=media(b)
print('%.2f'%mediab)

desviob=desvio(b)
print('%.2f'%desviob)


    