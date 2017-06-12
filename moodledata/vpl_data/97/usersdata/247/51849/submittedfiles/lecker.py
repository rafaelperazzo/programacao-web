lista1=[ ]
n=int(input('lista'))
for i in range(1,n+1,1):
    v=float(input('v: '))
    lista1.append(v)
lista2=[ ]
for i in range(1,n+1,1):
    v=float(input('v: '))
    lista2.append(v)
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
            elif i==len(lista)-1:
                if lista[i]>lista[i+1]:
                    cont=cont+1
            else:
                if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                    cont=cont+1
    if cont==1:
        return True
    else:
        return False
if lecker(lista1):
    print('N')
else:
    print('S')
if lecker(lista2):
    print('N')
else:
    print('S')