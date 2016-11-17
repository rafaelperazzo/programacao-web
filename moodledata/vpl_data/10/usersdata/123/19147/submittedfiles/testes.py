def cong(a,b,m,x0,n):
    lista=[]
    lista.append(x0)
    for i in range (0,n,1):
        valor= ((a*lista[i]+b)%m)/m
        lista.append(valor)
    del(lista[0])
    return lista

a=input('Insira a:')
b=input('Insira b:')
m=input('Insira m:')
x0=input('Insira x0:')
n=input('Insira n:')

print cong(a,b,m,x0,n)