a = int(input('Digite um número inteiro: '))
lista=[]
k=1
while k<=a:
    if (a%k)==0:
        lista = lista + [k]
    k=k+1
divisores=int(len(lista))
print('\nLista de divisores:')
print(lista)
print('\nQuantidade de divisores: %i' % divisores)