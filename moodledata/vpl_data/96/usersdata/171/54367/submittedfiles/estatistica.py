# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    n=len(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i]-media(lista))**2)
    dV = (soma2/(n-1))**(0.5)
    return dV
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('digite o numero de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor1=int(input('digite os numeros da lista a:'))
    a.append(valor1)
b=[]
for i in range(1,n+1,1):
     valor2=int(input('digite os numeros da lista a:'))
    a.append(valor2)
m1=media(a)
print('%.2f'%m1)
dv1=desvio(a)
print('%.2f'%dv1)
m2=media(b)
print('%.2f'%m2)
dv2=desvio(b)
print('%.2f'%dv2)    
