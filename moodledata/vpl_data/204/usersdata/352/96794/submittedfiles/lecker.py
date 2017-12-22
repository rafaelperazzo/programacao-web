# -*- coding: utf-8 -*-

def lecker(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1

    if cont==1:
        return (True)
    else:
        return(False)
    if lecker(lista):
        print('Sim')
    else:
        print('Não')


n=int(input('Quantidade de elementos: '))
lista_a=[ ]
lista_b=[ ]

for i in range(0,n,1):
    valor=float(input('Valor: '))
    lista_a.append(valor)

for i in range(0,n,1):
    valor=float(input('Valor: '))
    lista_b.append(valor)

