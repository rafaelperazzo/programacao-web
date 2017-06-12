lista=[]
n=int(input('tamanho:'))
for i in range(1,n+1,1):
    v=int(input('valores:'))
    lista.append(v)
for i in range(1,len(lista),1):
    if lista[i]>lista[i-1]:
        print('S')
    break in (len(lista)-1)/2