def mediageometrica(n):
    produto=0
    for i in range(0,len(n),1):
        produto=produto*n[i]
    resultado=(produto**(1/len(n)))
    return(resultado)
    
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    elementos=int(input('Digite o elemento da lista:'))
    a.append(elementos)
    
print('%.3f'%(mediageometrica(a)))