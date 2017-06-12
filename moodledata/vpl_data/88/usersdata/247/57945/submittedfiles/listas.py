import math
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
def degrau(lista):
    b=[ ]
    for i in range(0,len(lista)-1,1):
        diferença=math.ABS(lista[i]-lista[i+1])
        b.append(diferença)
    return(b)
def maiordegrau(lista):
    b=degrau(lista)
    m=maior(b)
    return (m)
print(maiordegrau(lista))