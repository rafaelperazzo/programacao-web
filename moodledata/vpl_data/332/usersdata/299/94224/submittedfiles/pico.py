# -*- coding: utf-8 -*-
def pico(lista):
    a=[]
    b=[]
    for i in range(1,len(lista),1):
    #CRIAR DUAS LISTAS, ANTES E DEPOIS DO SUPOSTO PICO
        if lista[i-1]<lista[i]:
            a.append(lista[i-1])
        elif lista[i-1]==lista[i]:
            return('N')
            break
        elif lista[i-1]>lista[i]:
            b.append(lista[i])
    #ANALISAR SE A LISTA INICIAL É CRESCENTE
    cont1=0
    for i in range(1,len(a),1):
        if a[i-1]<a[i]:
            cont1+=0
        else:
            cont1+=1
    #ANALISAR SE A LISTA FINAL É CRESCENTE
    cont2=0
    for i in range(1,len(b),1):
        if b[i-1]>b[i]:
            cont2+=0
        else:
            cont2+=1
    if cont1==0 and cont2==0:
        return('S')
    else:
        return('N')
    
#CODIGO PRINCIPAL

l=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i  in range(0,n,1):
    l.append(int(input('')))
print(pico(l))
    
    
