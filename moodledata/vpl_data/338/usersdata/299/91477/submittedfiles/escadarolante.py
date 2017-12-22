N=int(input(''))
cont=0
x=[]
for i in range(1,N+1,1):
    i=int(input(''))
    x+=[i]
    continue

# iniciais
cont+=x[1]-x[0]
#centrais
for i in range(2,N+1,1):
    if x[i]-x[i-1]<=10:
        cont+=x[i]-x[i-1]
    elif x[i]-x[i-1]>10:
        cont+=x[i]+10
#finais
print(cont+10)