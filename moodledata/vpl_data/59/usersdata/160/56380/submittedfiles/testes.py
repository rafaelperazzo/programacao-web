
    
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista:'))
    a.append(elementos)

p=1/n
    
prouto=0
for i in range(0,n,1):
    produto=produto*a[i]
resultado=produto**p

print('%.3f'%resultado)