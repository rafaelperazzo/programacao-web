lista=[]
cont=0

def pico(n,lista):
    for i in range(1,(n-1)/2,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==0:
        return('s')
    else:
        return('n')
        
    
    






n = (int(input('Digite a quantidade de elementos da lista: ')))
for i in range(0,n,1):
    lista.append(int(input('digite um valor%.d: ' )))
print(pico(n,(lista)))    
