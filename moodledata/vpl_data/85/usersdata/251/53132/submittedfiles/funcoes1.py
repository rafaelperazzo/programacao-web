# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            return(False)
    return(True)
    
#escreva as demais funções
def decrescente (lista):
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            return(False)
    return(True)




#escreva o programa principal
l1=[]
l2=[]
l3=[]
n=int(input('Digite o numero de termos das listas: '))

for i in range(0,n,1):
    termo=int(input('Digite o termo de índice '+str(i)+' da lista: '))
    l1.append(termo)
    
'''for i in range(0,n,1):
    termo=int(input('Digite o termo de índice '+str(i)+' da lista: '))
    l2.append(termo)''' 
    
'''for i in range(0,n,1):
    termo=int(input('Digite o termo de índice '+str(i)+' da lista: '))
    l3.append(termo)'''    
    
if crescente(l1):
    print('S')
else:
    print('N')
    
if decrescente(l1):
    print('S')
else:
    print('N')    