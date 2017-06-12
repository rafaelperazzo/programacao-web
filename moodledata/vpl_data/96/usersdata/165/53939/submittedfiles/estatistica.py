# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista):
    soma=0
    x=media(lista)
    for i in range(0,len(lista),1):
        soma=(lista[i]-x)**2
        
    desvio=(soma/(len(lista)-1))**(1/2)
    return(desvio)
    
    
n1=int(input('digite o tamanho de a:'))
n2=int(input('digite o tamanho de b:'))
a=[]
b=[]
for i in range(1,n1+1,1):
    valor=float(input('digite um valor:'))
    a.append(valor)
for i in range(1,n2+1,1):
    valor=float(input('digite um numero:'))
    b.append(valor)
    
print('%.2f' %media(a))
print('%.2f' %desvio(a))
print('%.2f' %media(b))
print('%.2f' %desvio(b))


