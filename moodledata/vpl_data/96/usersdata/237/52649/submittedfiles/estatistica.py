# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    so=0
    for i in range(0,len(lista),1):
        so=so+((lista[i]-media(lista))**2)
    resultado = (so/(len(lista)-1))**(1/2) 
    return resultado

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input("Digite n: "))
a=[]
b=[]
for i in range(0,n,1):
    a.append(int(input("Digite o termo: ")))
for i in range(0,n,1):
    b.append(int(input("Digite o termo: ")))
print('%.2f'%media(a))
print('%.2f'%desvio(a))
print('%.2f'%media(b))
print('%.2f'%desvio(b))