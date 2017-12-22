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
    for r in range(0,len(lista),1):
        soma=soma+((lista[r]-media(lista))**2)
    ola= ((soma/(len(lista) -1))**0.5)
    return ola

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('digite n: '))
a=[]
for j in range(0,n,1):
    x = int(input('digite: '))
    a.append(x)
b=[]    
for j in range(0,n,1):
    x = int(input('digite: '))
    b.append(x)
soma=0
for r in range(0,len(b),1):
    soma=soma+((b[r]-media(b))**2)
desvio2= ((soma/(len(b) -1))**0.5)

print('%.2f' %media(a))  
print('%.2f' %desvio(a))
print('%.2f' %media(b))
print('%.2f' %desvio2)