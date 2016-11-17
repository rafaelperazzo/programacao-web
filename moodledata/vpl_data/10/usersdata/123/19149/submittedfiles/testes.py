def cong(a,b,m,x0,n):
    x=[]
    x.append(x0)
    for i in range (0,n,1):
        valor= ((a*x[i]+b)%m)/m
        x.append(valor)
    del(x[0])
    return x

a=input('Insira a:')
b=input('Insira b:')
m=input('Insira m:')
x0=input('Insira x0:')
n=input('Insira n:')

print cong(a,b,m,x0,n)