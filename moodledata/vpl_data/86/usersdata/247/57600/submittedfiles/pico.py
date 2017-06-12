n=int(input('digite: '))
lista=[ ]
for i in range(1,n+1,1):
    valor=float(input('valor: '))
    lista.append(valor)
def pico(lista):
    for i in range(1,len(lista),1):
        if lista[0]>lista[1]:
            return False
        elif lista[i]>lista[i+1]:
            return False
        elif lista[i]>lista[i-1]:
            return False
        else:
            return True
if pico(lista):
    print('S')
else:
    print('N')
        
        