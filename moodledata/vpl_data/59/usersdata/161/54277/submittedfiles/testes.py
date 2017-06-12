
lista1=[]
lista2=[]
n=int(input('n'))
for i in range(1,n+1,1):
    num=int(input('num'))
    lista1.append(num)
for i in range(1,n+1,1):
    num=int(input('num'))
    lista2.append(num)    
    
def crescente(lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i] > lista[i-1]:
            cont=cont+1
        if cont==len(lista)-1:
            return True
        else:
            return False
if crescente(lista1):
    print('s')
else:
    print('n')
if crescente(lista2):
    print('s')
else:
    print('n')    
