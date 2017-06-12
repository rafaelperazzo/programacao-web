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

def media(lista1):
    soma1=0
    for i in range(0,len(lista1),1):
        soma1=soma1+lista1[i]
    media1=soma1/len(lista1)
    return(media1)
def media(lista1):
    soma1=0
    for i in range(0,len(lista2),1):
        soma2=soma2+lista2[i]
    media2=soma2/len(lista2)
    return(media2)
def desvpad1(media1,lista1):
    soma3=0
    for i in range(0,len(lista1),1):
        soma3=soma3+((lista[i]-media1)**2)
    desvio1=(soma3/(n-1))**(1/2)
    return(desvio1)
def desvpad2(media2,lista2):
    soma4=0
    for i in range(0,len(lista1),1):
        soma4=soma4+((lista[i]-media2)**2)
    desvio2=(soma4/(n-1))**(1/2)
    return(desvio2)    
print('%.2f'%(lista1))
print('%.2f'%desvpad1(lista1,media1(lista1))
print('%.2f'%(lista2))
print('%.2f'%desvpad2(lista2,media2(lista2))
    
    