n=int(input('Informe o tamanho da lista:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('Informe um número:'))
    lista.append(numero)
    
def semrepetiçao(lista):
    b=[]
    for i in range(0,len(lista),1):
        if lista[i] not in b:
            b.append(lista[i])
    return (b)

def vezes(b,lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==b:
            cont=cont+1
    return (cont)
    
def quantidade(lista,b):
    c=[]
    for i in range(0,len(b),1):
        c.append(vezes(b[i],lista))
    return(c)

def indicedomaior(c):
    maior=c[0]
    indice=0
    for i in range(0,len(c),1):
        if c[i]>maior:
            maior=c[i]
            indice=i
    return (indice)
    
def indicedomenor(c):
    menor=c[0]
    indice=0
    for i in range(0,len(c),1):
        if c[i]<menor:
            menor=c[i]
            indice=i
    return (indice)        

b=semrepetiçao(lista)
c=quantidade(lista,b)
maiorindice=indicedomaior(c)
print(b[maiorindice])
menorindice=indicedomenor(c)
print(b[menorindice])


        