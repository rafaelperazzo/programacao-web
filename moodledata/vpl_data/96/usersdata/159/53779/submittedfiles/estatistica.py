# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista,resultado):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-resultado)**2)
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

mediaa=media(a)   
mediab=media(b)
print('A média de a é: %.2f' %mediaa)
print('O desvio padrão de a é: %.2f' %desvio(a,mediaa))

print('A média de b é: %.2f' %media(b))
print('O desvio padrão de b é: %.2f' %desvio(b,mediab))