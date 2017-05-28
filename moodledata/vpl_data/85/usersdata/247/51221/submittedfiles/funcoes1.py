lista1=[ ]
n=int(input('numero de elementos da lista1: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    lista1.append(valor)
print(lista1)
lista2=[ ]
n=int(input('numero de elementos da lista2: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    lista2.append(valor)
print(lista2)
listaf=[ ]
n=int(input('numero de elementos da lista3: '))
for i in range(1,n+1,1):
    valor=int(input('valor: '))
    listaf.append(valor)
print(listaf)
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
        if lista[i]==lista[i+1]:
            cont-cont+1
    if cont!=0:
        return True
    else:
        return False
if crescente(lista1):
    print('S')
else:
    print('N')
if decrescente(lista1):
    print('S')
else:
    print('N')
if consecutivo(lista1):
    print('S')
else:
    print('N')
if crescente(lista2):
    print('S')
else:
    print('N')
if decrescente(lista2):
    print('S')
else:
    print('N')
if consecutivo(lista2):
    print('S')
else:
    print('N')
if crescente(lista3):
    print('S')
else:
    print('N')
if decrescente(lista3):
    print('S')
else:
    print('N')
if consecutivo(lista3):
    print('S')
else:
    print('N')