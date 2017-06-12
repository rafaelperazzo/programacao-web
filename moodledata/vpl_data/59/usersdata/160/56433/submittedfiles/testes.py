#Primeiramente definimos a função que irá nos dar a média aritmética geométrica
#A função agm, vai receber 3 parâmetros que são indexados pelo usuário na entrada
def agm(a,b,erro):
    
    while (abs(a-b)>erro):
        a1=((0.5)*(a+b))
        b1=(a*b)**0.5
    return(a1,b1)
    
    
#        
n=int(input('Digite a quantidade de elementos da lista:'))
erro=float(input('Digite o erro:'))

#Criação e pedidos de lista para a execução
a=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista a:'))
    a.append(elementos)
b=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista b:'))
    b.append(elementos)

#o que vai ser imprimido para o usuário
print(agm(a,b,erro))