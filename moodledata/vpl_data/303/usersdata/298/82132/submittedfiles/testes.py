b = int(input('Digite um número inteiro: '))
c = int(input('Digite um número inteiro: '))
d = int(input('Digite um número inteiro: '))

lista1=[]
k1=1
while k1<=b:
    if (b%k1)==0:
        lista1=lista1+ [k1]
    k1=k1+1
    
lista2=[]
k2=1
while k2<=c:
    if (c%k2)==0:
        lista2=lista2+ [k2]
    k2=k2+1
    
lista3=[]
k3=1
while k3<=d:
    if (d%k3)==0:
        lista3=lista3+ [k3]
    k3=k3+1
    
for div1 in lista1:
    for div2 in lista2:
        for div3 in lista3:
            for div1 in div2:
                for div1 in div3:
                    print(div1)

print('\nMáximo divisor comum:')
print(mdc)

#---------------------------------------------------------------------------------------------------------------------
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