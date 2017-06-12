lista=[]
n=int(input('tamanho:'))
for i in range(1,n+1,1):
    v=int(input('valores:'))
    lista.append(v)
p=(len(lista)-1)/2
for i in range(1,lista[p],1):
    if lista[i]>lista[i-1]:
        print('S')