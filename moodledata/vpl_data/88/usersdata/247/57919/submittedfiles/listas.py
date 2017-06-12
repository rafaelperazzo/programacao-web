lista=[ ]
n=int(input('digite: '))
for i in range(1,n+1,1):
    valor=float(input('valor '))
    lista.append(valor)
def maior(lista):
    maior=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
    return maior
