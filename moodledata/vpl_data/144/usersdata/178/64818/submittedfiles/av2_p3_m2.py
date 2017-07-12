# -*- coding: utf-8 -*-


def vezes (n,lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==n:
            cont=cont+1
    return (cont)
    
def magica(lista):
    cont=0
    for i in range(0,len,(lista),1):
        if vezes(i,lista)==lista[i]:
            cont=cont+1
    if cont==len(lista):
        return true
    else:
        return false
        
        
n=int(input('Digite o tamanho:'))
a=[]
for i in range(0,n,1):
    x=int(input('Digite o elemento:'))
    a.append(x)
if magica[a]:
    print ('SIM')
else:
    print ('NÃO')
        
        
        
        
        
