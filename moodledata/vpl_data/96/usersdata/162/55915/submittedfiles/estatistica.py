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
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1 + lista[i]
    media=soma1/len(lista)
    return (media)

def desvpad(lista,media):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]-media)**2)
    desvio=(soma2/(n-1))**(0.5)
    return(desvio)

print('%.2f'%media(lista1))
print('%.2f'%desvpad(lista1,media(lista1)))
print('%.2f'%media(lista2))
print('%.2f'%desvpad(lista2,media(lista2)))
