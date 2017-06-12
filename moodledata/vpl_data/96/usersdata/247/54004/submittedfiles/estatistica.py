n=int(input('digite n: '))
lista1=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista1.append(valor)
lista2=[ ]
for i in range(0,n,1):
    valor=float(input('digite n: '))
    lista2.append(valor)
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
def desvio(lista):
    soma=0
    n=len(lista)
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    desvio=((soma/n+1)**0,5)
    return desvio
print('%.2f' %media(lista1))
print('%.2f' %desvio(lista1))
print('%.2f' %media(lista2))
print('%.2f' %desvio(lista2))
