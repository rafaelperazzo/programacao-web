# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def desvpadrao(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + (lista[i]-media(lista))**2
    resultado = (soma/(len(lista)-1))**(0,5)
    return resultado

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('escreva o numero de elementos das listas:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o numero a ser anexado a lista:'))
    a.append(valor)
b=[]    
for i in range(0,n,1):
    valor=int(input('digite o numero a ser anexado a segunda lista:'))
    b.append(valor)
    
mediaa=media(a)
print('%.2f'%mediaa)

desvioa=desvpadrao(a)
print('%.2f'%desvioa)

mediab=media(b)
print('%.2f'%mediab)

desviob=desvpadrao(b)
print('%.2f'%desviob)

    