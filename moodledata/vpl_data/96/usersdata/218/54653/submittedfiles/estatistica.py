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
        soma=soma+((lista[i]-media(lista))**2)
    d=(soma/(len(lista)-1))**0,5
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('escreva o numero de elementos das listas:'))
a=[]
for i in range(0,n,1):
    valor=float(input('digite o numero a ser anexado a lista:'))
    a.append(valor)
b=[]    
for i in range(0,n,1):
    valor=float(input('digite o numero a ser anexado a segunda lista:'))
    b.append(valor)
    
ma=media(a)
print('%.2f'%ma)

da=desvio(a)
print('%.3f'%da)

mb=media(b)
print('%.2f'%mb)

db= desvio(b)
print('%.3f'%db)

    