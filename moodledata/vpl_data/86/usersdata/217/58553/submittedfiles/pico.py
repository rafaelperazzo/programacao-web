# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    cont=0
    
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    p=((len(lista)-1)/2)
    for i in range(1,len(lista),1):
        if i>=p:
            if lista[i]<lista[i-1]:
                cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
            
        
n = int(input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
lis=[]
for i in range(1,n+1,1):
    j=int(input('digite j:'))
    lis.append(j)
if pico(lis):
    print('S')
else:
    print('N')
