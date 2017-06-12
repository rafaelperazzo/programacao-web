# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista):
    soma=0
    media=media(lista)
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    
    desvio=(soma/len(lista)-1)**0.5
    return desvio
    
qa=int(input('Quantidade de elementos da lista a:'))
a=[]

for i in range (0,qa,1):
    valor=float(input('Valor:'))
    a.append(valor)

qb=int(input('Quantidade de elementos da lista b:'))
b=[]

for i in range (0,qb,1):
    valor=float(input('Valor:'))
    b.append(valor)

print('%.2f' %media(a))
print('%.2f' %desvio(a))

print('%.2f' %media(b))
print('%.2f' %desvio(b))