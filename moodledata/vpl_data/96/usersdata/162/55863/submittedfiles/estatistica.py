# -*- coding: utf-8 -*-

n=int(input('Digite n:'))
lista1=[]
lista2=[]
for i in range(0,n,1):
    a=float(input('termos:'))
    lista1.append(a)
for i in range(0,n,1):
    b=float(input('termos:'))
    lista2.append(b)
def media1(lista1):
    soma1=0
    for i in range(0,len(lista1),1):
        soma1=soma1 + lista1[i]
    media1=soma1/len(lista1)
    return (media1)
def media2(lista2):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+lista2[i]
    media2=soma2/len(lista2)
    return(media2)
def desvpad1(media1,lista1):
    soma3=0
    for i in range(0,len(lista1),1):
        soma3=soma3+((lista[i]-media1)**2)
    desvio1=(soma3/(n-1))**(0.5)
    return(desvio1)
def desvpad2(media2,lista2):    
    soma4=0
    for i in range(0,len(lista),1):
        soma4=soma4+((lista[i]-media2)**2)
    desvio2=(soma4/(n-1))**(0.5)
    return(desvio2)
print('%.2f'%media1(lista1))
print('%.2f'%desvpad1(lista1,media1(lista1)))
print('%.2f'%media2(lista2))
print('%.2f'%desvpad2(lista2,media2(lista2)))
