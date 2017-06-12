n=int(input('digite: '))
lista=[ ]
for i in range(1,n+1,1):
    valor=float(input('valor: '))
    lista.append(valor)
def pico(lista):
    cont=0
    for i in range(1,len(lista)//2,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    for i in range((len(lista)//2)+1,len(lista,1):
        if lista[i]<lista[i-i]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
if pico(lista):
    print('S')
else:
    print('N')
        
        