n = int(input('Digite um numero inteiro positivo entre 1 e 100: '))
while (n<1) and (n>100):
    print('Entrada inválida.')
    n = int(input('Digite um numero inteiro positivo entre 1 e 100: '))
if n in range (1,100):
    kn = float(((n + 2)/10)*2)
    print('%.4f' % kn)
    
#-----------------------------------------------------------------------------------------------------------------------
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))

listan1 = []
kn1 = 1
while (kn1<=n1*n2*n3):
    multiplo1 = n1*kn1
    listan1 = listan1 + [multiplo1]
    kn1 = kn1 + 1

listan2 = []
kn2 = 1
while (kn2<=n1*n2*n3):
    multiplo2 = n2*kn2
    listan2 = listan2 + [multiplo2]
    kn2 = kn2 + 1
    
listan3 = []
kn3 = 1
while (kn3<=n1*n2*n3):
    multiplo3 = n3*kn3
    listan3 = listan3 + [multiplo3]
    kn3 = kn3 + 1
    
listapreliminar = [i for i in listan1 if i in listan2]
listafinal = [i for i in listapreliminar if i in listan3]
mmc = listafinal[0]

print('\nO mmc é:')
print(mmc)
print('\n')
#---------------------------------------------------------------------------------------------------------------------------
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
    
listapreliminar = [i for i in lista1 if i in lista2]
listafinal = [i for i in listapreliminar if i in lista3]
mdc = listafinal[(len(listafinal) - 1)]

print('\nMáximo divisor comum:')
print(mdc)
print('\n')

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