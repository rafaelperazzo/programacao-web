# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('qte de termos:'))
lista1=[]
lista2=[]
for i in range(0,n,1):
    t1=float(input('termo de 1:'))
    lista1.append(t1)
for i in range(0,n,1):
    t2=float(input('termo de 2:'))
    lista2.append(t2)    

def media(lista):
    soma1=0
    for i in range(0,len(lista1),1):
        soma1=soma1+lista1[i]
    media=soma1/len(lista1)
    return(media)

def desvpad(media,lista):
    soma3=0
    for i in range(0,len(lista),1):
        soma3=soma3+((lista[i]-media)**2)
    desvio1=(soma3/(n-1))**(1/2)
    return(desvio)
    
print('%.2f'%(lista1))
print('%.2f'%desvpad(lista1,media(lista1))
print('%.2f'%(lista2))
print('%.2f'%desvpad(lista2,media(lista2))
    
    