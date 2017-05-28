lista1=[ ]
n=int(input('numero de elementos da lista: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    lista1.append(valor)
print(lista1)
lista2=[ ]
n=int(input('numero de elementos da lista: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    lista2.append(valor)
lista3=[ ]
n=int(input('numero de elementos da lista: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    lista3.append(valor)
def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def consecutivo(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]=lista[i+1]:
            cont-cont+1