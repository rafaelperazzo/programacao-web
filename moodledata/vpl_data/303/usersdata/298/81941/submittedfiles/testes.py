a = int(input('Digite um numero inteiro: '))
lista=[]
k=1
while k<=a:
    if (a%k)==0:
        lista = lista + [k]
    k=k+1
divisores=int(len(lista))
print('Lista de divisores:')
print(lista)
print('\n Quantidade de divisores: %i' % divisores)