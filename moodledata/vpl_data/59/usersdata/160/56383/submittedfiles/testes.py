#Definindo a função para a média geométrica
def mediageometrica(n):
    #p=raiz 
    p=1/n
    produto=0
    for i in range(0,len(n),1):
        produto=produto*n[i]
    resultado=produto**p
    return(resultado)

n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista:'))
    a.append(elementos)

print('%.3f'%resultado)



def mediageometrica(n):
    p=1/n
    produto=0
    for i in range(0,len(n),1):
        produto=produto*n[i]
    resultado=produto**p
    return(resultado)