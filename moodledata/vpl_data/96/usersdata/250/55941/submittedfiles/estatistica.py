# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
def desPad(lista):
    soma=0
    soma1=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
        media=soma/(len(lista))
        soma1=soma1+(lista[i]-media)**2
        desPad=((soma1/n-1))**(1/2)
    return desPad
n=int(input('tamanho da lista:'))
a=[]
b=[]
for i in range (0,n,1):
    a.append(int(input('valores da primeira lista:')))
for i in range (0,n,1):
    b.append(int(input('valores da segunda lista:')))   
media_a=media(a) 
desPad_a=desPad(a)
media_b=media(b)
desPad_b=desPad(b)
print(media_a)
print(desPad_a)
print(media_b)
print(desPad_b)
    
