def agm(a,b,erro):
    while (abs(a-b)>erro):
        a1=((0.5)*(a+b))
        b1=(a*b)**0.5
    return(a1,b1)
        
n=int(input('Digite a quantidade de elementos da lista:'))
erro=float(input('Digite o erro:'))
a=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista a:'))
    a.append(elementos)
b=[]
for i in range(1,n+1,1):
    elementos=float(input('Digite o elemento da lista b:'))
    b.append(elementos)

print(agm(a,b,erro))