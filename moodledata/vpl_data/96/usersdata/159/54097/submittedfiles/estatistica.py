# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista,media):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media)**2)
    
    desvio=(soma/len(lista)-1)**0.5
    return desvio
    
n=int(input('Quantidade de elementos das listas:'))
a=[]

for i in range (0,n,1):
    valor=(input('Valor:'))
    a.append(valor)

b=[]

for i in range (0,n,1):
    valor=(input('Valor:'))
    b.append(valor)

ma= media(a)
da= desvio(a,ma)
mb= media(b)
db= desvio(b,mb)

print('%.2f'%ma)
print('%.2f'%da)
print('%.2f'%mb)
print('%.2f'%db)