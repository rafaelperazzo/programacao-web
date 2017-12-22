# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
a=[]
n1=int(input('Digite a quantidade de termos: '))
soma1=0

for i in range (0,n,1):
    numero1=int(input('Digite o numero: '))
    a.append(numero)
    soma1=soma1+numero

media1=soma1/n1
somatorio1=0

for l in range(0,n,1):
    somatorio1=somatorio1+((a(l)-media1))**2

desvio1=((1)/(n-1)*(somatorio1)**0.5

#para a lista 2




print('%.2f'% a[0])
print('%.2f'% a[n-1])
print('%.2f'% media1)   
print('%.2f'% desvio1)




#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 