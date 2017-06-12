
lista1=[]
lista2=[]
n=int(input('n'))
def crescente(lista):
    cont=0
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
